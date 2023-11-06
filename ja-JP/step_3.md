## 顔の形

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
顔やマスクの形を描いて色を付けます。 他の機能はまだ追加しないでください。後で追加されます。
</div>
<div>
！[四角いロボットの画像。](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

マスクの顔の主な形を決定します。 円、楕円、長方形、さらには三角形の場合もあります。

`draw()`関数にコードを追加して、顔またはマスクを描画します。

この例では、中央に円を描きますが、どの形状を使用するかはあなた次第です。

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 12
---

def draw(): # Put code to run every frame here background(255, 255, 255)  # Change to your background colour

    # Add code to draw your face here
    ellipse(width/2, height/2, 200, 200)  # Circle in the middle
    
    grid()  # add a # to the beginning of this line to hide the grid

--- /code ---

![グリッドの中央に黒い円が表示されている出力領域。](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**テスト：** コードを実行して変更し、必要な顔のサイズと形状を取得します。

--- /task ---

--- task ---

アウトラインにはストロークの色を選択し、シェイプの主要部分には塗りつぶしの色を選択します。

[[[processing-stroke]]]

アウトラインが必要ない場合は、`no_stroke()`を使用します。

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 13
---

    def draw():
      stroke(0) #no_stroke()を使用することもできます 
      fill(255, 255, 0) #鮮明な黄色
      ellipse(width/2, height/2, 200, 200) #真ん中の円

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**テスト：** コードを実行し、満足するまで色を変更します。

--- /task ---

--- save ---
