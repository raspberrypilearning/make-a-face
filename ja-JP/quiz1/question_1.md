## ふりかえり

お疲れさまでした。たくさんのことを学びましたね！ 次はふりかえりの時間です。ふりかえりを行うことで、脳内に新しいつながりを作ることができます。このため、ふりかえりは学習の大事な部分です。

以下の3つの質問に答えて、学んだことをふりかえってみましょう。

各質問の後、**答えを確認する**を押してください。 正しい答えが表示されます。 このアクティビティは何度でも実行できます。

お楽しみください!

--- question ---

---
凡例：質問1/3
---

プロジェクトでは、図形で口を描きました。

このコードはどのような口を描くでしょうか？

--- code ---
---
language: python

---
def draw(): fill(0, 0, 0) #Black ellipse(160, 200, 150, 150) fill(255, 255, 255) #White ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  あといっぽ、悲しい口を作成するには、 2番目の `ellipse` には、最初の `ellipse` より低い**y_coordinate**が必要です。

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  そのとおりです！ 2番目の `ellipse` は、最初の `ellipse` より高い **y_coordinate**で描画されます。

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   あといっぽ、2番目の円には白の `fill(255, 255, 255)` があり、最初の黒の円の上に部分的に配置されています。

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

コードは長方形を描画しません。 `ellipse` ファンクションは円を描画します。

  --- /feedback ---

--- /choices ---

--- /question ---
