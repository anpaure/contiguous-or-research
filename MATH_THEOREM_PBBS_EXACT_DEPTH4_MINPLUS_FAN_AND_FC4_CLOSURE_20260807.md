# The depth-four min-plus fan has thirteen rays, and every actual binomial margin is positive

**Date:** 2026-08-07  
**Status:** unconditional classification of the complete $D=4$ covering-price
fan and unconditional verification of $FC_4$ for every actual
coefficient-one binomial instance.  The classification is by an explicit
Apéry normal form, not by a numerical fan search.  No $FC_D$ conclusion
for $D\ge5$ is claimed.

## 1. The closed four-piece cone

Write a closed piece-cost table in increment coordinates as

\[
 (p_1,p_2,p_3,p_4)
 =(a,a+b,a+b+c,a+b+c+d).
 \tag{1.1}
\]

Monotonicity and subadditivity on lengths at most four are equivalent to

\[
 \boxed{
 a\ge0,\quad 0\le b,c,d\le a,\quad c+d\le a+b.}
 \tag{1.2}
\]

Let

\[
 \psi_p(L)=\min\left\{
 x_1p_1+x_2p_2+x_3p_3+x_4p_4:
 x_i\in\mathbb Z_{\ge0},\ \sum_{i=1}^4ix_i=L
 \right\}.
 \tag{1.3}
\]

The size-two density is never strictly best, since (1.2) gives

\[
                         p_4\le2p_2.
 \tag{1.4}
\]

Also $p_i\le ip_1$.  Thus one may always choose a minimum-density
denomination from $\{3,4\}$.  Their comparison is

\[
 {p_3\over3}\lesseqgtr{p_4\over4}
 \quad\Longleftrightarrow\quad
 a+b+c\lesseqgtr3d.
 \tag{1.5}
\]

This already reduces the fan to two residue systems.

## 2. Finite Apéry certificate

Suppose denomination $h\in\{3,4\}$ has minimum density and put

\[
                         e_i=p_i-{i\over h}p_h\ge0.
 \tag{2.1}
\]

In the residue graph $\mathbb Z/h\mathbb Z$, a size-$i$ piece is an
edge of reduced cost $e_i$.  A minimum reduced-cost walk may be made
simple by deleting every subwalk between two repeated residues.  Hence it
uses at most $h-1$ non-$h$ pieces.  Its total ordinary length is at
most nine when $h=4$, and at most eight when $h=3$.

Consequently:

1. all transient choices occur at lengths at most nine;
2. after the chosen residue representative becomes available,
   $\psi_p(L+h)=\psi_p(L)+p_h$; and
3. the complete infinite min-plus fan is determined by the finite simple
   residue paths just described.

The following tables give the resulting exact certificate.

## 3. Eight maximal cones

Let $\mathcal B$ be the cone (1.2).  On the side
$a+b+c\ge3d$, choose denomination four; on the other side choose
denomination three.  The eight rows below cover $\mathcal B$, with
overlap only on fan walls.

\[
\begin{array}{c|l|l}
 &\text{additional conditions inside }\mathcal B
 &\text{extreme-ray indices from (4.1)}\\ \hline
 A_1&a+b+c\ge3d,\ d\le b,\ d\le c
     &1,3,4,6,8\\
 A_2&a+b+c\ge3d,\ b\le d\le c
     &1,3,8,9\\
 A_3&a+b+c\ge3d,\ c\le d\le b,\ 2d\le b+c
     &1,4,8,12\\
 A_4&a+b+c\ge3d,\ c\le d\le b,\ b+c\le2d
     &1,8,10,12,13\\
 A_5&a+b+c\ge3d,\ b\le d,\ c\le d
     &1,8,9,10,11\\ \hline
 B_1&a+b+c\le3d,\ d\le b
     &5,8,10,13\\
 B_2&a+b+c\le3d,\ b\le d,\ 2d\le a+b
     &5,7,8,9,10,11\\
 B_3&a+b+c\le3d,\ b\le d,\ a+b\le2d
     &2,5,7,8,9
\end{array}
 \tag{3.1}
\]

The coverage is an elementary case split.  On the four-density side,
order $d$ relative to $b,c$; in the only remaining order
$c\le d\le b$, split at $2d=b+c$.  On the three-density side, first
split at $d=b$, then at $2d=a+b$.  Eliminating the displayed
inequalities gives exactly the ray generators in the last column.

Here is a simultaneous optimal partition on each cone.  The notation
$i^q$ means $q$ pieces of size $i$; a missing exponent is one.
These are common optimizers at every generating ray, so they prove that
$p\mapsto\psi_p(L)$ is linear on each cone.

\[
\begin{array}{c|l}
A_1&L=4q+r:\quad4^q+r\quad(0\le r\le3)\\
A_2&4q:4^q;\quad
     4q+1:1\ (q=0),\ 4^{q-1}+2+3\ (q\ge1);\\
   &4q+2:4^q+2;\quad4q+3:4^q+3\\
A_3&4q:4^q;\quad4q+1:4^q+1;\\
   &4q+2:2\ (q=0),\ 4^{q-1}+3^2\ (q\ge1);\quad
     4q+3:4^q+3\\
A_4&4q:4^q;\quad
     4q+1:1\ (q=0),\ 1+4\ (q=1),\ 4^{q-2}+3^3\ (q\ge2);\\
   &4q+2:2\ (q=0),\ 4^{q-1}+3^2\ (q\ge1);\quad
     4q+3:4^q+3\\
A_5&4q:4^q;\quad
     4q+1:1\ (q=0),\ 2+3\ (q=1),\ 4^{q-2}+3^3\ (q\ge2);\\
   &4q+2:2\ (q=0),\ 4^{q-1}+3^2\ (q\ge1);\quad
     4q+3:4^q+3\\ \hline
B_1&3q:3^q;\quad3q+1:1\ (q=0),\ 3^{q-1}+4\ (q\ge1);\\
   &3q+2:2\ (q=0),\ 1+4\ (q=1),\ 3^{q-2}+4^2\ (q\ge2)\\
B_2&3q:3^q;\quad3q+1:1\ (q=0),\ 3^{q-1}+4\ (q\ge1);\\
   &3q+2:2\ (q=0),\ 2+3\ (q=1),\ 3^{q-2}+4^2\ (q\ge2)\\
B_3&3q:3^q;\quad3q+1:1\ (q=0),\ 3^{q-1}+4\ (q\ge1);\quad
     3q+2:3^q+2
\end{array}
 \tag{3.2}
\]

For completeness, optimality of (3.2) is a finite hand check: subtract
as many minimum-density (h)-pieces as possible, and compare the simple
residue paths of (2.1).  There are at most three non-four pieces in the
$A$-rows and at most two non-three pieces in the $B$-rows.  The path
comparisons reduce exactly to the inequalities in (3.1).  No length above
nine introduces a new comparison by Section 2.

## 4. The thirteen rays and their complete closures

The primitive increment rays and their closed tables are

\[
\begin{array}{c|c|c|l}
i&(a,b,c,d)&(p_1,p_2,p_3,p_4)&\psi_i(L)\\ \hline
1 &(1,0,0,0)&(1,1,1,1)&\lceil L/4\rceil\\
2 &(1,0,0,1)&(1,1,1,2)&\lceil L/3\rceil\\
3 &(1,0,1,0)&(1,1,2,2)&\lceil L/2\rceil\\
4 &(1,1,0,0)&(1,2,2,2)&2q+\min(r,2),\quad L=4q+r\\
5 &(1,1,0,1)&(1,2,2,3)&\lceil2L/3\rceil\\
6 &(1,1,1,0)&(1,2,3,3)&\lceil3L/4\rceil\\
7 &(2,0,0,1)&(2,2,2,3)&\lceil2L/3\rceil+\mathbf1_{L=1}\\
8 &(1,1,1,1)&(1,2,3,4)&L\\
9 &(2,0,1,1)&(2,2,3,4)&L+\mathbf1_{L=1}\\
10&(2,1,0,1)&(2,3,3,4)&L+\mathbf1_{L\in\{1,2,5\}}\\
11&(3,0,0,1)&(3,3,3,4)&L+2\mathbf1_{L=1}
                                      +\mathbf1_{L\in\{2,5\}}\\
12&(2,2,0,1)&(2,4,4,5)&\lceil5L/4\rceil+\mathbf1_{L=2}\\
13&(3,3,0,2)&(3,6,6,8)&2L+\mathbf1_{L\in\{1,5\}}
                                      +2\mathbf1_{L=2}
\end{array}
 \tag{4.1}
\]

The first, second, third, fourth, fifth, sixth and eighth rays are the
seven extreme rays of the original closed-table cone (1.2).  The other
six are created by refinement with the min-plus residue walls.

The simplest genuinely mixed ray is ray 7.  Its formula follows without
any enumeration.  Every piece in the table $(2,2,2,3)$ costs at least
$2/3$ times its length.  Equality with the integer lower bound is
attained by size-three pieces, with one size-two piece for residue two,
and, for a positive residue-one length, one size-four piece replacing one
size-three piece.  Only $L=1$ is exceptional.  It is a genuine fan ray:
the independent walls

\[
 b=0,\qquad c=0,\qquad p_2+2p_3=2p_4
 \quad\Longleftrightarrow\quad a+b=2d
 \tag{4.2}
\]

cut out $(a,b,c,d)=(2,0,0,1)$.

Equations (3.1)--(3.2) prove both completeness and extremality of (4.1):
the eight cones cover (1.2), each listed generator is an extreme generator
of at least one cone, and a common optimal configuration makes the closure
linear on that cone.

## 5. Exact binomial margin formula

For an actual depth-four instance put

\[
 r=\left\lceil{k\over2}\right\rceil,\qquad t=r-4,\qquad
 H_s={k\choose s}-{k\choose s-1},
 \tag{5.1}
\]

and use the nonempty-ideal birth convention

\[
 \widetilde H_1=k,\qquad \widetilde H_b=H_b\quad(b\ge2).
 \tag{5.2}
\]

For any one of the explicit functions in (4.1), its supply price minus
its canonical whole-job price is

\[
 \boxed{
 M_k(\psi)=
 \sum_{u=1}^4H_{t+u}\psi(u)
 -\sum_{b=1}^{t-1}\widetilde H_b\psi(t-b).}
 \tag{5.3}
\]

Thus every entry below is reproducible using only four additions on the
left, the displayed formula for $\psi_i$, and binomial coefficients.  As
an independent check, if $a_q=\psi(q)-\psi(q-1)$, the same integer is

\[
 \sum_{q=1}^{t-1}
 \left[
 \mathbf1_{q\le4}
 \left({k\choose r}-{k\choose t+q-1}\right)
 -\mathbf1_{q<t}{k\choose t-q}
 \right]a_q,
 \tag{5.4}
\]

where the $q=t-1$ job term is $k$, not $H_1$.  Equations
(5.3) and (5.4) are two hand-checkable forms of the worksheet.

## 6. The first mixed margin

Ray 7 differs from ray 5 only at job length one.  Therefore

\[
 \boxed{
 M_k(\psi_7)=M_k(\psi_5)+H_{t+1}-H_{t-1}.}
 \tag{6.1}
\]

The correction is positive throughout the actual depth-four range.  For
even $k=2r$, $t=r-4$,

\[
 {H_{r-3}\over H_{r-5}}
 ={7(r+5)(r+6)\over11(r-4)(r-3)}\ge1
 \quad\Longleftrightarrow\quad r\le39.
 \tag{6.2}
\]

For odd $k=2m+1$, $t=m-3$,

\[
 {H_{m-2}\over H_{m-4}}
 ={3(m+5)(m+6)\over5(m-3)(m-2)}\ge1
 \quad\Longleftrightarrow\quad m\le30.
 \tag{6.3}
\]

Actual depth-four rows have only $r\le25$ and $m\le19$.  Hence the
first genuinely mixed wall costs positive margin rather than exposing a
separator.

## 7. Exact depth-four worksheet

Write $M_i=M_k(\psi_i)$.  Direct substitution in (5.3) gives:

| $k$ | $M_1$ | $M_2$ | $M_3$ | $M_4$ | $M_5$ | $M_6$ | $M_7$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 23 | 614836 | 607729 | 789176 | 1048524 | 1039899 | 1222864 | 1222565 |
| 25 | 2063100 | 2022320 | 2628600 | 3511640 | 3460485 | 4077140 | 4085395 |
| 27 | 6854433 | 6636255 | 8637918 | 11637213 | 11355504 | 13420698 | 13490364 |
| 29 | 22456034 | 21346900 | 27834983 | 37985070 | 36516046 | 43364019 | 43799686 |
| 31 | 72113285 | 66688254 | 87140938 | 121311494 | 113962138 | 136339147 | 138774538 |
| 32 | 242892254 | 270900568 | 344286836 | 431180116 | 456693270 | 532574698 | 513761790 |
| 33 | 224894274 | 199139226 | 260869928 | 375073960 | 339474396 | 411049614 | 423836556 |
| 34 | 839065840 | 933111066 | 1184230935 | 1489213060 | 1570208865 | 1834378155 | 1771944465 |
| 35 | 670338323 | 550914139 | 724020058 | 1101922833 | 933849664 | 1155604568 | 1219947424 |
| 36 | 2873528192 | 3183093723 | 4031631266 | 5098763987 | 5342550551 | 6256867061 | 6055044011 |
| 37 | 1850689754 | 1307308605 | 1726795883 | 2960240130 | 2183006845 | 2836346259 | 3149962255 |
| 38 | 9728928000 | 10718957905 | 13536595965 | 17255753454 | 17923869114 | 21063421419 | 20437953180 |
| 39 | 4379716640 | 1945178430 | 2608920688 | 6558350084 | 3024664344 | 4787554132 | 6278184900 |
| 40 | 32438627234 | 35469061914 | 44597574446 | 57494347726 | 58986917181 | 69653294938 | 67848779115 |
| 42 | 105909966679 | 114535228149 | 143055611619 | 187490741269 | 188914287959 | 224636386209 | 220112187867 |
| 44 | 335588925788 | 356893565179 | 441029249438 | 592873552547 | 581011003356 | 698313876197 | 690672794386 |
| 46 | 1016267694530 | 1051530093932 | 1275506279645 | 1788901070204 | 1673552155721 | 2048139655319 | 2058280418937 |
| 48 | 2854147410644 | 2805588781509 | 3277065259296 | 4988801214336 | 4264498187717 | 5411719062988 | 5611047108973 |
| 50 | 6908321675367 | 5992776747559 | 6274012037349 | 11874886247399 | 7958701930416 | 11240576609381 | 12657802271456 |

| $k$ | $M_8$ | $M_9$ | $M_{10}$ | $M_{11}$ | $M_{12}$ | $M_{13}$ |
|---:|---:|---:|---:|---:|---:|---:|
| 23 | 1214009 | 1396675 | 1654735 | 1837401 | 2088423 | 3128322 |
| 25 | 4023985 | 4648895 | 5523585 | 6148495 | 6972125 | 10432610 |
| 27 | 13124337 | 15259197 | 18209937 | 20344797 | 22992690 | 34348194 |
| 29 | 41799585 | 49083225 | 58972080 | 66255720 | 74500739 | 111016785 |
| 31 | 128418957 | 153231357 | 186075423 | 210887823 | 235269602 | 349231740 |
| 32 | 557378108 | 614446628 | 699585524 | 756654044 | 887868922 | 1344562192 |
| 33 | 372245145 | 456607305 | 564368637 | 648730797 | 714512859 | 1053987222 |
| 34 | 1911293399 | 2113028999 | 2409274671 | 2611010271 | 3059381499 | 4629590330 |
| 35 | 970401417 | 1256499177 | 1604187427 | 1890285187 | 2035499630 | 2969348734 |
| 36 | 6478370483 | 7190863943 | 8216078149 | 8928571609 | 10440995821 | 15783545778 |
| 37 | 1971050865 | 2938006275 | 4033689495 | 5000644905 | 5141350355 | 7324350096 |
| 38 | 21614733629 | 24128817695 | 27652789381 | 30166873447 | 35177355431 | 53101216812 |
| 39 | 815150697 | 4068671253 | 7404307833 | 10657828389 | 9570814565 | 12595405758 |
| 40 | 70553565803 | 79415427737 | 91425462865 | 100287324799 | 116466369077 | 175453204708 |
| 42 | 223137179429 | 254335079337 | 294823515039 | 326021414947 | 376313137322 | 565226685682 |
| 44 | 672352314533 | 782014105563 | 916593942900 | 1026255733930 | 1173345921477 | 1754350938589 |
| 46 | 1866066185369 | 2250794448585 | 2689775530194 | 3074503793410 | 3459426274723 | 5132934110387 |
| 48 | 4376728218623 | 5723277139879 | 7118340182303 | 8464889103559 | 9236878127795 | 13501070899454 |
| 50 | 5897775548573 | 10596875889613 | 14865039370733 | 19564139711773 | 19747120825515 | 27703838520881 |

Every entry is strictly positive.

The optimal-depth definition

\[
 D=\min\left\{d:
 d{ k\choose r}+{d+1\choose2}
 \ge\sum_{j=1}^{r-1}{k\choose j}\right\}
 \tag{7.1}
\]

gives $D=4$ exactly for

\[
 \{23,25,27,29,31,32,33,34,35,36,37,38,39,40,
   42,44,46,48,50\}.
 \tag{7.2}
\]

This list is itself a direct substitution in (7.1).  Here is a standalone
check that there are no later rows.  Put

\[
 A_r={4^r\over2{2r\choose r}},
 \qquad {A_{r+1}\over A_r}={2(r+1)\over2r+1}>1.
 \tag{7.3}
\]

For $k=2r-1$ and $k=2r$, respectively,

\[
 {\Lambda\over W}=A_r-{1\over W},
 \qquad
 {\Lambda\over W}=A_r-{1\over2}-{1\over W}.
 \tag{7.4}
\]

Both parity subsequences are strictly increasing, since $A_r$ and $W$
increase.  At $k=51,52$, the exact values of
$\Lambda-4W-10$ are, respectively,

\[
 134062840946405,\qquad 20166415418769,
 \tag{7.5}
\]

so (7.1) forces depth at least five there and on every later row of the
same parity.

### Theorem 7.1 (exact depth-four closure)

For every complete coefficient-one binomial instance of optimal depth
$D=4$, every nonnegative covering-price inequality holds.  Equivalently,
the whole-job configuration LP $FC_4$ is feasible.

#### Proof

Sections 2--4 reduce all covering prices to the thirteen rays in (4.1).
Section 7 verifies a strictly positive margin on every ray for every
actual depth-four row.  Linearity on each of the eight fan cones makes the
margin nonnegative for every closed price.  The exact configuration-price
separation theorem then gives $FC_4$. \(\square\)

Any admissible deletion profile whose retained rank histogram remains
nondecreasing inherits the same conclusion, because the signed-tail
deletion formula adds

\[
 \sum_{s<t}\beta_s
 \bigl(\psi(t-s)-\psi(t-s-1)\bigr)\ge0
\tag{7.6}
\]

to every margin.

## 8. General finite-state pattern

The Apéry reduction is not special to four.

### Proposition 8.1 (finite min-plus fan at every fixed depth)

Fix $D$, and let $p_1,\ldots,p_D$ be a nonnegative closed piece-cost
table.  Choose any denomination $h$ minimizing $p_i/i$.  In the
reduced-cost residue graph modulo $h$, a shortest path may be chosen
simple.  It therefore has at most $h-1$ edges and ordinary length at
most

\[
                         D(h-1)\le D(D-1).
 \tag{8.1}
\]

For each residue, once that representative is available,

\[
                         \psi(L+h)=\psi(L)+p_h.
 \tag{8.2}
\]

Consequently the complete infinite covering closure is determined by
finitely many comparisons at lengths at most $D(D-1)$.  The closed
price cone is cut into a finite rational polyhedral fan indexed by
minimum-density denominations and finite shortest-path policies.

#### Proof

Put $e_i=p_i-ip_h/h\ge0$.  Every partition is a walk in
$\mathbb Z/h\mathbb Z$ with the same reduced cost.  If a walk repeats a
residue, delete the intervening cycle; its reduced cost is nonnegative and
its ordinary length is a multiple of $h$.  Iteration leaves a simple
walk with at most $h-1$ edges.  Adding the required number of $h$-pieces
then proves (8.2).  Every policy comparison is linear in $p$, so their
finite common refinement is rational polyhedral. \(\square\)

This proposition explains both the success and the limitation of the
depth-four calculation.  The all-depth obstruction is no longer an
infinite sequence of job lengths; it is a growing but finite family of
shortest-path policies, together with the need to prove their binomial
margins uniformly as $D\sim\sqrt{k}$.  The symmetric two-step Pascal
pairing theorem gives a second finite-state description on the binomial
side.  What is still missing is a positivity invariant coupling these two
finite-state systems.
