## テーマを選択してください

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
作りたい顔やマスクのアイデアはありますか？ この手順を使用して、アートを計画し、キャンバスを設定します。
</div>
<div>
![吸血鬼をテーマにした顔の出力領域。](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

[スタータープロジェクト](https://trinket.io/library/trinkets/54d15b9cdf){:target="_blank"}を開きます。 Trinketは別のブラウザタブで開きます。

--- /task ---

--- task ---

**選択：** あなたが作りたい顔の種類について考えてください：
+ あなたの遺産や大衆文化から何かを選びたいですか？
+ あなたのアートは、人間、動物、何か神話的なもの、あるいはおそらく機械を示していますか？
+ 自画像を作成することもできます。
+ 絵文字を描いて友達と共有することができます

--- /task ---

--- task ---

最初にPython `Processing library` を使用してアートを作成するときにすることは、`def setup():` を追加して、プログラムの開始時に`def setup():` 関数を定義することです。

スタータープロジェクトには、`setup`関数でキャンバスの `size` を `400` 幅および`400` 高さに設定できます。

**選択：** 数値を試してコードを実行し、満足のいくサイズを見つけます。

--- collapse ---

---
title: プログラム起動時の画面サイズの設定
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():   
    size(400, 400) #400x400は丸い顔に適しています

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**選択：** 顔に使用する色について考え、 `の背景` 色の値を変更して、画面を補色に設定します。

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: プログラム開始時の背景色の設定
---

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 9
line_highlights: 9
---
    background(255, 255, 255) #色を変えるために別の数字を試してください

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**ヒント：** `draw` 関数には`grid()`コードがあります。 これにより、背景に座標グリッドが追加され、顔のどこにフィーチャを配置するかを決めるのに役立ちます。

グリッドをオフにするには、コードの前に `＃` を追加し、オンに戻すには、 `＃`を削除します。

--- code ---
---
language: python
filename: main.py - draw()
---
    grid() #グリッドを表示 

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---
    #grid() #コメントに変えてグリッドを非表示にする 

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを実行して、選択した画面サイズと背景色を確認します。

--- /task ---


--- task ---

**デバッグ：** プロジェクトに修正が必要なバグが見つかる場合があります。 一般的なバグは次のとおりです。

--- collapse ---

---
title: サイズと色を更新しましたが、出力領域は同じままです
---

コードを変更した後、出力領域の変更を確認するには、プロジェクトを`run`実行する必要があります。

--- /collapse ---

--- collapse ---

---
タイトル: 数字を変えたのに、背景の色が変更されない。
---

赤、緑、青それぞれの最大値は`255`です。 `background`に指定したそれぞれの値が`0`から`255`の間に入っていることを確認してください。

--- /collapse ---

--- /task ---

--- save ---
