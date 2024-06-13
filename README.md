Sub SetTableBorderColorToBlack()  
    Dim tbl As Table  
    Dim bdr As Borders  
    Dim style1 As Style  
    Dim style2 As Style  
    Dim style3 As Style
    Dim cell As Cell
    Dim head_font As String
    head_font="黑体" 
    ' 获取标题1样式  
    Set style1 = ActiveDocument.Styles("标题 1")  
    With style1.Font  
        .Name = head_font ' 设置字体为黑体  
        .Size = 16 ' 近似设置为三号字大小（16磅）  
    End With  
      
    ' 获取标题2样式  
    Set style2 = ActiveDocument.Styles("标题 2")  
    With style2.Font  
        .Name = head_font ' 保持当前默认字体，或者你也可以指定一个字体名  
        .Size = 14 ' 近似设置为四号字大小（14磅）  
    End With  
      
    ' 获取标题3样式  
    Set style3 = ActiveDocument.Styles("标题 3")  
    With style3.Font  
        .Name = head_font ' 保持当前默认字体，或者你也可以指定一个字体名  
        .Size = 14 ' 近似设置为四号字大小（14磅）  
    End With  
      
    ' 显示消息框，告知操作完成  
    MsgBox "标题样式已更新"  
    ' 遍历文档中的所有表格  
    For Each tbl In ActiveDocument.Tables  
        ' 获取表格的边框对象  
        Set bdr = tbl.Borders  
        For Each cell In tbl.Range.Cells  
			With cell.Range.ParagraphFormat
                .Alignment = wdAlignParagraphCenter ' 水平居中
            End With
 			cell.Range.Font.Name = "宋体"  
            cell.Range.Font.Size = 10.5 
            ' 清除单元格的背景颜色  
            cell.Shading.BackgroundPatternColorIndex = wdWhite ' 设置为背景色为白色，相当于清除背景色  
        Next cell  
        ' 设置边框颜色为黑色  
        With bdr  
            .InsideColor = wdColorBlack ' 内部边框颜色设置为黑色  
            .OutsideColor = wdColorBlack ' 外部边框颜色设置为黑色  
        End With  
    Next tbl  
    MsgBox "表格文字已全部居中"
    ' 显示消息框，告知操作完成  
	MsgBox "所有表格背景颜色已清除"  
    MsgBox "所有表格边框颜色已设置为黑色"  
End Sub
