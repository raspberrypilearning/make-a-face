--- question ---

---
凡例：質問2/3
---

プロジェクトでは、多くの機能を備えた顔を描くためのコードを追加しました。 顔をデザインのように見せるためには、コードの順序が非常に重要でした。

このコードを実行した場合、顔はどのようになりますか？

--- code ---
---
language: python

---

def draw():

  #Face stroke(0) #Black fill(255) #White ellipse(200, 200, 200, 190) no_stroke()

  #Eyes fill(0, 255, 0) #Green ellipse(160, 180, 60, 60) ellipse(240, 180, 60, 60) fill(0) #Black ellipse(160, 180, 30, 30) ellipse(240, 180, 30, 30)

run()

--- /code ---

--- choices ---

- ( )

![黒の輪郭を持つ白い顔。 黒い輪郭で緑色の目が2つあります。](images/face1.png)

 --- feedback ---

 あといっぽ、 `ellipse()` と `stroke()` ファンクションの順序を見てください。

 --- /feedback ---

- ( )

![黒の輪郭を持つ白い顔。 二つ黒瞳孔の緑目があり、両方とも黒い輪郭を持っています。](images/face2.png)

 --- feedback ---

 あといっぽ、 `stroke()` ファンクションの順序を見てください。

 --- /feedback ---

- (x)

![黒の輪郭を持つ白い顔。 瞳孔が黒い緑色の目が2つあり、目には輪郭がありません。](images/face3.png)

 --- feedback ---

 正解です。コードは黒いストロークで顔を描画し、円を描画する前にストロークをオフにします。 緑の円が最初に描画され、その上に黒の円が描画されます。

 --- /feedback ---

- ( )

![黒の輪郭を持つ白い顔。 輪郭のない緑色の目が2つあります。](images/face4.png)

 --- feedback ---

 あといっぽ、 `ellipse()` ファンクションの順序を見てください。

 --- /feedback ---

--- /choices ---

--- /question ---
