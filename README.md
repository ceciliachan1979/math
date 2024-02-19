# math

Posting some math related latex documents

# FAQ on LaTeX

## 如果我不懂LaTeX怎麼辦？

* 安裝LaTeX：

    * 一般Linux有 pdflatex command 可使用。

    * Windows: https://miktex.org/ , https://www.texniccenter.org/

* Quick Start: https://latex-tutorial.com/tutorials/amsmath/

* Quick Reference: https://en.wikipedia.org/wiki/Help:Displaying_a_formula

* Docker:

    如果你不想安裝LaTeX，可以使用Docker。以下是一個例子：

    * 下載：`docker pull ghcr.io/xu-cheng/texlive-full:latest`

    * 編譯：`docker run --rm -it -v $(pwd):/src -w /src/Books/BabyRudin ghcr.io/xu-cheng/texlive-full:latest latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode ./BabyRudin.tex`

    * 開啟：`open ./Books/BabyRudin/BabyRudin.pdf`

## 用電腦typeset數學證明是學習數學證明的最佳方法嗎？

不，根據研究（ref: https://www.youtube.com/watch?v=7PQbidoBPBc ），手寫對長遠記憶的效果更好。可是，如果你想別人看到你的練習／作品，或者方便保存日後參考／分享，使用 LaTeX 吧！

## 其他資源：

https://www.texmacs.org
