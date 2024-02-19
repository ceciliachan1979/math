# math

Posting some math related latex documents

# Books
- [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf), Eric Lehman, F Thomson Leighton, Albert R Meyer
- [Algorithm Design](https://www.amazon.com/gp/product/0321295358/), Jon Kleinberg, Eva Tardos
- [Combinatorial Optimization: Algorithms and Complexity](https://www.amazon.com/Combinatorial-Optimization-Algorithms-Complexity-Computer/dp/0486402584), Christos H. Papadimitriou, Kenneth Steiglitz
- [Principles of Mathematical Analysis](https://maa.org/press/maa-reviews/principles-of-mathematical-analysis), Walter Rudin
- [Basic Analysis: Introduction to Real Analysis](https://www.jirka.org/ra/), Jiří Lebl
- [Analysis I](https://link.springer.com/book/10.1007/978-981-19-7261-4), Terence Tao
- [Understanding Analysis](https://link.springer.com/book/10.1007/978-1-4939-2712-8), Stephen Abbott
- [Problems in Mathematical Analysis](https://www.amazon.com/Problems-Mathematical-Analysis-Boris-Demidovich/dp/B0007BNL1W), Boris Demidovich
- [A Problem Book in Real Analysis](https://link.springer.com/book/10.1007/978-1-4419-1296-1), Asuman G. Aksoy, Mohamed A. Khamsi
- [Linear Algebra Done Right](https://linear.axler.net/), Sheldon Axler
- [Linear Algebra Done Wrong](https://www.math.brown.edu/streil/papers/LADW/LADW.html), Sergei Treil
- [Abstract Algebra: Theory and Applications](http://abstract.ups.edu/download.html), Thomas W. Judson, Robert A. Beezer
- [Measure Theory](https://link.springer.com/book/10.1007/978-1-4614-6956-8), Donald L. Cohn
- [Algebraic Number Theory](https://link.springer.com/book/10.1007/978-3-662-03983-0), Jürgen Neukirch

# Papers
- [Mathematical method and proof](https://www.andrew.cmu.edu/user/avigad/Papers/method.pdf), [Jeremy Avigad](https://www.andrew.cmu.edu/user/avigad/)

# Courses
- [Calculus 1](https://ocw.aca.ntu.edu.tw/ntu-ocw/ocw/cou/104S115), Chen-Yu Chi, NTU OCW
- [Calculus 2](https://ocw.aca.ntu.edu.tw/ntu-ocw/ocw/cou/104S210), Chen-Yu Chi, NTU OCW
- [Analytics](https://ocw.aca.ntu.edu.tw/ntu-ocw/ocw/cou/105S107), Chen-Yu Chi, NTU OCW
- [Advanced Calculus 1](https://ocw.nthu.edu.tw/ocw/index.php?page=course&cid=204&), Shu-Jung Kao, NTHU OCW
- [Advanced Calculus 2](https://ocw.nthu.edu.tw/ocw/index.php?page=course&cid=225&), Shu-Jung Kao, NTHU OCW
- [Advanced Calculus 1](https://ocw.nycu.edu.tw/?course_page=all-course%2Fcollege-of-science%2Fam%2Fadvanced-calculus-i-97), Chi-Kaung Pai, NYCU OCW
- [Advanced Calculus 2](https://ocw.nycu.edu.tw/?course_page=all-course%2Fcollege-of-science%2Fam%2Fadvanced-calculus-ii-97), Chi-Kaung Pai, NYCU OCW
- [Real Analysis](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/), Casey Rodriguez, MIT OCW
- [Probability Theory and Stochastic Processes](https://mathweb.ucsd.edu/~tkemp/ProbabilityTube/), Todd Kemp

# YouTube Channel
- [The Bright Side of Mathematics](https://www.youtube.com/@brightsideofmaths)
- [James Cook](https://www.youtube.com/@jamescook5617)

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

# References
- [Graphic notes on Gilbert Strang's "Linear Algebra for Everyone"](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/)
