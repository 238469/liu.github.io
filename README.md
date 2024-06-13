

```vb
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
```

```vb
Sub SetTableBorderColorToBlack()     
    Dim normalStyle As Object
    Dim fontSize As Single
      
    ' 假设正文的默认样式是“正文”或“Normal”，这里使用“Normal”作为示例
    Set normalStyle = ActiveDocument.Styles("正文")
      
    ' "小四"字号在VBA中通常对应12磅，但你可以根据实际需要调整这个值
    fontSize = 12
      
    With normalStyle.Font
        .Name = "宋体" ' 设置字体为宋体
        .Size = fontSize ' 设置字体大小为12磅
    End With
    MsgBox "正文字体已更改为宋体小四" 
End Sub
```

```vb
Sub CenterTableText()
    Dim tbl As Table
    Dim cell As cell
      
    ' 遍历文档中的所有表格
    For Each tbl In ActiveDocument.Tables
        ' 遍历表格中的所有单元格
        For Each cell In tbl.Range.Cells
            ' 设置单元格内容的水平和垂直对齐方式
            With cell.Range.ParagraphFormat
                .Alignment = wdAlignParagraphCenter ' 水平居中
            End With
              
            ' cell.VerticalAlignment = wdCellAlignVerticalCenter ' 垂直居中（WPS中可能不支持这个属性）
              
        Next cell
    Next tbl
      
    ' 显示消息框，告知操作完成
    MsgBox "表格文字已全部居中"
End Sub
```

```vbscript
Sub CenterTableText()
    Dim tbl As Table
    Dim cell As cell
      
    ' 遍历文档中的所有表格
    For Each tbl In ActiveDocument.Tables
        ' 遍历表格中的所有单元格
        For Each cell In tbl.Range.Cells
            ' 设置单元格内容的水平和垂直对齐方式
           	cell.Range.Font.Name = "宋体"  
            cell.Range.Font.Size = 10.5 
              
            ' cell.VerticalAlignment = wdCellAlignVerticalCenter ' 垂直居中（WPS中可能不支持这个属性）
              
        Next cell
    Next tbl
      
    ' 显示消息框，告知操作完成
    MsgBox "表格文字全部为宋体1"
End Sub
```

```vbscript
Sub ChangeMainTextFontToSongTi()  
    Dim para As Paragraph  
      
    ' 遍历文档中的所有段落  
    For Each para In ActiveDocument.Paragraphs  
        ' 检查段落的样式名称是否为“正文”  
        If para.Style = ActiveDocument.Styles("正文") Then  
            With para.Range.Font  
                .Name = "宋体"  
                ' 如果需要，你也可以设置字体大小等其他属性  
            End With  
        End If  
    Next para  
    Dim tbl As Table
    Dim cell As cell
      
    ' 遍历文档中的所有表格
    For Each tbl In ActiveDocument.Tables
        ' 遍历表格中的所有单元格
        For Each cell In tbl.Range.Cells
            ' 设置单元格内容的水平和垂直对齐方式
           	cell.Range.Font.Name = "宋体"  
            cell.Range.Font.Size = 10.5 
              
            ' cell.VerticalAlignment = wdCellAlignVerticalCenter ' 垂直居中（WPS中可能不支持这个属性）
              
        Next cell
    Next tbl
      
    ' 显示消息框，告知操作完成
    MsgBox "表格文字全部为宋体1"
End Sub
```

```vbscript
Sub ChangeMainTextFontToSongTiExceptFirstPage()  
    Dim para As Paragraph  
    Dim tbl As Table  
    Dim cell As Cell  
    Dim isFirstPage As Boolean  
    Dim bookmarkFirstPage As Bookmark  
      
    ' 假设你已经在第一页的末尾插入了一个名为"EndOfFirstPage"的书签  
    On Error Resume Next ' 忽略找不到书签的错误  
    Set bookmarkFirstPage = ActiveDocument.Bookmarks("_Toc355702769")  
    On Error GoTo 0 ' 恢复正常的错误处理  
      
    ' 遍历文档中的所有段落  
    isFirstPage = True  
    For Each para In ActiveDocument.Paragraphs  
        ' 如果找到了书签，那么从下一个段落开始不再视为第一页内容  
        If Not bookmarkFirstPage Is Nothing And para.Range.Start >= bookmarkFirstPage.Range.Start Then  
            isFirstPage = False  
        End If  
          
        ' 如果不是第一页的内容，并且段落的样式为“正文”，则修改字体  
        If Not isFirstPage And para.Style = ActiveDocument.Styles("正文") Then  
            With para.Range.Font  
                .Name = "宋体"  
                .Size = 10.5 ' 设置字体大小等其他属性  
            End With  
        End If  
    Next para  
      
    ' 遍历文档中的所有表格  
    isFirstPage = True  
    For Each tbl In ActiveDocument.Tables  
        ' 检查表格是否在第一页（这里使用表格的第一个单元格的位置来判断）  
        If Not bookmarkFirstPage Is Nothing And tbl.Cell(1, 1).Range.Start >= bookmarkFirstPage.Range.Start Then  
            isFirstPage = False  
        End If  
          
        ' 如果不是第一页的内容，则修改表格中所有单元格的字体  
        If Not isFirstPage Then  
            For Each cell In tbl.Range.Cells  
                With cell.Range.Font  
                    .Name = "宋体"  
                End With  
            Next cell  
        End If  
    Next tbl  
      
    ' 显示消息框，告知操作完成  
    MsgBox "表格和正文文字（除第一页外）已全部更改为宋体10.5"  
End Sub
```

![image-20240612111433939](D:\图片存放位置\image-20240612111433939.png)
