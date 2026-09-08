# Full status cubes versus the two-colour product-SCD atlas

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

There are two different conclusions.

1.  The full split-pair status-cube partition by itself gives an exact
    owner-disjoint cycle factor on all but an exponentially small middle
    leave.  With the two-scale rotor installed in each retained subcube,
    every window through the protected height is geodesic, every active
    direction crosses the prescribed two-colour split, and the number of
    components is

    \[
                         O(W/H^2)+2^{-\Omega(m)}W
                         =o(W/m)                     \tag{0.1}
    \]

    whenever \(H/\sqrt m\to\infty\) and
    \(H\log H=o(m)\).  Lower and upper shadows are simple *inside each
    status subcube*.  This is a complete owner/component theorem, not a
    global target theorem.

2.  The monotone paths of the two-colour product-SCD atlas cannot simply
    be retained and joined at their endpoints by status-orientation
    edges while inheriting their ordered shadow atlas.  A status edge can
    join two endpoints only when their complete ternary status words are
    identical and their orientation words differ in one bit.  Even if the
    resulting endpoint Hall problem is soluble, all but \(O(W/m)\) of
    the required seams are nonneutral already at depth one.  More
    strongly, if all monotone path edges are retained, the seams force
    at least

    \[
      \left(\kappa+o(1)\right)W,
      \qquad
      \kappa=2\operatorname{erf}(\sqrt{\log2})
              -{2\sqrt{\log2}\over\sqrt\pi}>0,       \tag{0.2}
    \]

    ordered mixed-collar occurrences which duplicate canonical monotone
    shadow occurrences, summed over depths \(q\le H\).  Thus endpoint
    stitching does not have \(o(W)\) one-copy ordered-shadow defect.

The last assertion is deliberately not a floor-corrected CPM no-go.  At
Gaussian depths a target may legitimately receive more than one copy.
What is closed is the proposed direct inheritance of W's one-copy
ordered atlas.  A positive synthesis must replace a positive density of
the monotone path chronology by bulk mixed-colour trades; endpoint seams
alone cannot do it.

## 1. Exact full-status cells

First take a fixed split

\[
                        A\mathbin{\dot\cup}B,
                        \qquad |A|=|B|=m,             \tag{1.1}
\]

and a bijection \(\pi:A\to B\).  For a middle owner \(X\), give each
pair \(\{a,\pi(a)\}\) one of the statuses

\[
 0=\text{empty},\qquad 2=\text{full},\qquad *=\text{split}. \tag{1.2}
\]

If the status is split, record its orientation bit, according as the
present coordinate lies in \(A\) or in \(B\).  A fixed ternary status
word with \(e\) stars is an isometric physical \(Q_e\): toggling one
orientation bit deletes one coordinate in one half and inserts its mate
in the other half.

At middle rank, if \(z,f,e\) are the numbers of empty, full, and split
pairs, then

\[
                         z=f,\qquad e=m-2f.           \tag{1.3}
\]

Consequently the exact number of middle status cells is

\[
                         S_m=[x^m](1+x+x^2)^m,        \tag{1.4}
\]

and in particular \(S_m\le3^m=o(W/m)\), where
\(W=\binom{2m}{m}\).

The same conclusion holds for logarithmic macroblocks with
rank-dependent pairings.  Indeed, in a block of \(d\) pairs, an arbitrary
pairing \(\pi_k\) at local rank \(k\) has the rank/status enumerator

\[
       \sum_{k,e}\#\{X:|X|=k,\ e(X)=e\}x^ky^e
                         =(1+x^2+2xy)^d.             \tag{1.5}
\]

This is independent of \(\pi_k\).  Toggling an orientation preserves
the local rank, so both endpoints continue to use the same pairing.
Tensoring the block cells and freezing the residual coordinates is
therefore an exact partition of the global middle layer.  Every cube
axis crosses the two prescribed halves.  If each half is a union of old
quartets, every axis also crosses old quartets.

Put \(P=d\lfloor m/d\rfloor\) and let \(\rho=2m-2P<2d\) be the number
of residual coordinates.  If \(e(X)\) is the total split dimension, then

\[
 \sum_X x^{|X|}y^{e(X)}
                  =(1+x)^\rho(1+x^2+2xy)^P.          \tag{1.6}
\]

In particular

\[
 \mathbb E(e\mid |X|=m)={Pm\over2m-1},              \tag{1.7}
\]

and

\[
 \mathbb E(e(e-1)\mid |X|=m)
 ={P(P-1)m(m-1)\over(2m-1)(2m-3)}.                 \tag{1.8}
\]

Thus \(e=P/2+O_{\mathbb P}(\sqrt m)\).  A completely elementary tail
bound, sufficient below, is obtained without conditioning estimates:

\[
 \#\{X:|X|=m,\ e(X)<t\}
 \le 2^{P+\rho}\sum_{e<t}\binom Pe.                \tag{1.9}
\]

For \(t=o(m)\), \(d=O(\log m)\), the right side is
\(2^{m+o(m)}=2^{-m+o(m)}W\).

## 2. Exact owner cycles and their component count

Let

\[
 h=2^{\lceil\log_2H\rceil},\qquad
 s=\log_2h,\qquad t=hs.                             \tag{2.1}
\]

The power-of-two correction in (2.1) is necessary: the phase map used by
the rotor exists because \(h\mid2^s\), in fact \(h=2^s\).  The often
written value \(H\lceil\log_2H\rceil\) is exact only when \(H\) is a
power of two.

In every status cell of dimension \(e\ge t\), retain a predetermined
set of \(t\) star positions, chosen from the status word and hence
independent of all orientation bits.  Freeze the other \(e-t\)
orientations.  This partitions the cell into physical \(Q_t\)'s.

Partition the \(t\) axes into \(h\) groups of size \(s\).  In group
\(i\), choose an oriented Hamilton cycle \(P_i\) of \(Q_s\), of length
\(2^s=h\), and let \(c_i\) be its cyclic phase.  For
\(x=(x_0,\ldots,x_{h-1})\), set

\[
 \sigma(x)=\sum_i c_i(x_i)\pmod h,                  \tag{2.2}
\]

and advance group \(\sigma(x)\) by one step of \(P_{\sigma(x)}\).
Call the resulting permutation \(R\).  Then

\[
 \sigma(Rx)=\sigma(x)+1,
 \qquad R^h=P_0\times\cdots\times P_{h-1}.          \tag{2.3}
\]

If \(R^nx=x\), (2.3) first forces \(h\mid n\), say \(n=hr\), and then
forces \(h\mid r\).  Hence every \(R\)-cycle has exact length \(h^2\).
Every window of at most \(h\) steps visits distinct groups, hence uses
distinct physical pair axes and is geodesic.

For either sign, the shadow map is injective inside one retained
subcube.  A lower flag marks a touched group by its one-unit rank
deficit; the missing pair marks the toggled cube coordinate, and the
oriented Hamilton cycle recovers its directed tail.  An upper flag gives
the identical recovery with a doubled pair.  Untouched groups and every
frozen coordinate are visible literally.

Let \(G\) be the number of retained middle owners and \(B=W-G\).  The
number of retained owner cycles is exactly \(G/h^2\).  By (1.9), if
\(H\log H=o(m)\), then

\[
                         B=2^{-m+o(m)}W.             \tag{2.4}
\]

Thus, even if every exceptional owner is covered separately,

\[
 \#\text{components}\le {W\over h^2}+B
                         =o(W/m)                    \tag{2.5}
\]

when \(H/\sqrt m\to\infty\).  This proves the owner/component part of
the proposed synthesis.  It does not compare shadows emitted by two
different status subcubes.

## 3. Product-SCD path endpoints and their status words

Fix SCDs of \(2^A\) and \(2^B\).  Let

\[
 C_a\subset\cdots\subset C_{m-a},
 \qquad D_b\subset\cdots\subset D_{m-b}.            \tag{3.1}
\]

At global middle rank, the product rectangle has one monotone path

\[
 C_i\cup D_{m-i},qquad
       \ell_0\le i\le m-\ell_0,qquad
       \ell_0=\max(a,b).                            \tag{3.2}
\]

Its low and high endpoints are

\[
 C_{\ell_0}\cup D_{m-\ell_0},qquad
 C_{m-\ell_0}\cup D_{\ell_0},                      \tag{3.3}
\]

and its length is

\[
                         L(a,b)=m-2\max(a,b).        \tag{3.4}
\]

Put

\[
 n_a=\binom ma-\binom m{a-1},qquad
 c_m=\binom m{\lfloor m/2\rfloor}.                 \tag{3.5}
\]

The number of monotone paths is

\[
                         N=c_m^2
  =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}. \tag{3.6}
\]

The number whose two chain starts agree is

\[
                         D=\sum_a n_a^2
                          =(1+o(1)){W\over m}.        \tag{3.7}
\]

For reference, (3.7) follows from

\[
 n_a=\binom ma{m-2a+1\over m-a+1}                  \tag{3.8}
\]

and the central scaling \(a=m/2-y\sqrt m\):

\[
 n_a^2=(1+o(1)){32y^2\over\pi m^2}
                    4^m e^{-4y^2}.                 \tag{3.9}
\]

The Riemann sum uses
\(\int_0^\infty y^2e^{-4y^2}\,dy=\sqrt\pi/32\).

Relative to a status pairing \(\pi\), an endpoint has the full label

\[
                  (\eta,\epsilon),qquad
 \eta\in\{0,2,*\}^m,\qquad
 \epsilon\in\{0,1\}^{\eta^{-1}(*)}.                \tag{3.10}
\]

Two endpoints can be joined by a status-orientation edge if and only if
their ternary words \(\eta\) are identical and their orientation words
differ in exactly one coordinate.  Thus the exact endpoint selection
problem decomposes over status cells.  If
\(E_\eta^{\rm lo},E_\eta^{\rm hi}\subseteq Q_{e(\eta)}\) are the low
and high endpoint sets, every proposed seam matching must pass the
ordinary hypercube Hall cuts

\[
 |N_{Q_e}(S)\cap E_\eta^{\rm side}|
                         \ge |S|                    \tag{3.11}
\]

between the two orientation parities, with the evident degree-two
modification for a zero-length path.  In particular it leaves at least

\[
 \left|\sum_{X\in E_\eta^{\rm side}}
                   (-1)^{|X\cap A|}\right|          \tag{3.12}
\]

endpoints in that cell unless other endpoint types are allowed to mix.
Neither the abundance of star positions nor W's rectangle theorem
implies (3.11).  This is the exact status-Hall gate for literal endpoint
stitching.

## 4. Depth-one neutral seams are confined to diagonal rectangles

Retain every edge of every monotone path and add cross edges only between
its endpoints.  Since the path cover has \(W-N\) edges, any resulting
2-factor must add exactly \(N\) seams.

Call a seam *bi-clean* if both its lower and upper shadows are holes of
the original W edge atlas.  Such a seam adds no duplicate at depth one.

### Lemma 4.1 (diagonal-endpoint necessity)

Except for endpoints of paths of length at most two, every bi-clean seam
can be charged to an endpoint of a rectangle with equal chain starts
\(a=b\).  Consequently the number of bi-clean seams is at most

\[
                         2D+o(N)=O(W/m).             \tag{4.1}
\]

#### Proof

Consider a high--high seam.  Its endpoints have adjacent values of
\(\ell_0\); write them as \(X\) at stratum \(l\) and \(Y\) at stratum
\(l+1\), so \(|X\cap A|=m-l\) and
\(|Y\cap A|=m-l-1\).  Then

\[
 R=X\cap Y=(Y\cap A)\cup(X\cap B),
 \quad
 U=X\cup Y=(X\cap A)\cup(Y\cap B).                 \tag{4.2}
\]

The lower shadow \(R\) is a W-hole exactly when its \(A\)-component is
a chain top (away from the central zero-length exception).  This says
that the rectangle of \(Y\) has \(A\)-start \(l+1\).  The upper shadow
\(U\) is a W-hole exactly when the \(B\)-component of \(Y\) is a chain
bottom, saying that its \(B\)-start is \(l+1\).  Both conditions hold
only when the two starts of \(Y\)'s rectangle agree.

For a low--low seam, the same calculation charges the endpoint at the
larger \(P=|X\cap A|\) value and again forces equal starts.  A low
endpoint can be adjacent to a high endpoint only within distance two of
the central \(P\)-level.  The number of paths involved is
\(O(N/m)=o(N)\), by (3.5).  Every diagonal path has two endpoints, so
(4.1) follows. \(\square\)

Thus at least \(N-O(W/m)\) seams necessarily disturb one of W's two
depth-one shadow resolutions.  This is only \(o(W)\), so Lemma 4.1 alone
is not a coefficient-one obstruction.  The ordered collars give a
stronger aggregate statement.

## 5. Every nondiagonal seam has a full canonical collision collar

### Lemma 5.1 (one-sided collar collision)

Join two same-side endpoints at adjacent strata and let \(Q\) be the
path at the larger stratum.  Write its chain starts as \((a,b)\), put
\(l=\max(a,b)\), and let

\[
                         L_Q=m-2l.                  \tag{5.1}
\]

If \(a\ne b\), then for every

\[
                         1\le q\le L_Q+1            \tag{5.2}
\]

the segment consisting of the seam and the first \(q-1\) edges of
\(Q\) has a lower or upper shadow which is also represented by a pure
monotone W \(q\)-window.  The sign is upper when the relevant high
endpoint has \(a>b\), lower when it has \(b>a\); at a low endpoint the
two signs are interchanged.

#### Proof

Take a high--high seam, and suppose first that \(a>b\).  Let \(Y\) be
the high endpoint of \(Q\), and let \(X\) be the adjacent high endpoint
at the preceding stratum.  Thus

\[
 Y=C^Q_{m-a}\cup D^Q_a,qquad
 X_A=Y_A+\alpha,qquad Y_B=X_B+\beta.               \tag{5.3}
\]

After the seam, traverse \(q-1\) edges of \(Q\) toward its low end.  The
upper shadow of these \(q+1\) owners is

\[
                         U_q=X_A\cup D^Q_{a+q-1}.    \tag{5.4}
\]

The set \(X_A\) belongs to a chain whose start is at most \(a-1\), so
it has at least

\[
                         m-2a+2\ge q                \tag{5.5}
\]

predecessors.  The second component in (5.4) has
\(a+q-1-b\ge q\) predecessors.  The ordered product-SCD flag theorem
therefore gives a pure monotone \(q\)-window with upper shadow \(U_q\).
It is distinct from the mixed window because the seam joins two
different monotone path components.

If \(b>a\), the lower shadow is

\[
                         L_q=C^Q_{m-b-q+1}\cup X_B.  \tag{5.6}
\]

Its two components have at least \(b-a+q-1\ge q\) and
\(m-2b+2\ge q\) successors, so the lower form of the same theorem
applies.

At a low--low seam let \(X\) be the low endpoint of \(Q\), let \(Y\)
be the adjacent endpoint at the preceding stratum, and traverse from
\(X\) toward the high end of \(Q\).  If \(a>b\), the mixed lower
shadow is

\[
                         Y_A\cup D^Q_{m-a-q+1}.     \tag{5.7}
\]

The two successor distances are at least \(m-2a+2\) and
\(a-b+q-1\), respectively.  If \(b>a\), the mixed upper shadow is

\[
                         C^Q_{b+q-1}\cup Y_B,        \tag{5.8}
\]

and the two predecessor distances are at least \(b-a+q-1\) and
\(m-2b+2\).  Thus the same canonical-window argument applies in both
cases.  This proves the lemma. \(\square\)

The lemma uses no property of the seam beyond being a cross edge between
the specified endpoints.  It therefore applies a fortiori to every
status-orientation seam.

## 6. A linear aggregate collision invariant

Give every same-side seam the path at its larger stratum as its charged
path.  A path receives at most two charges, one at each endpoint.
Low--high seams use only paths of length at most two and account for
\(o(N)\) charges.  By (3.7), diagonal paths account for at most
\(2D=o(N)\) further charges.  Hence Lemma 5.1 applies to
\(N-o(N)\) charges.

It remains to minimize the sum of the charged path lengths subject to
capacity two per path.  Under the uniform distribution on the \(N\)
product paths, the two chain starts are independent with weights
\(n_a/c_m\).  If

\[
 Y={m/2-a\over\sqrt m},                             \tag{6.1}
\]

then (3.8) and the local central estimate give the limiting density

\[
                         f_Y(y)=4ye^{-2y^2},\qquad y\ge0. \tag{6.2}
\]

For two independent starts, the normalized path length

\[
                         T={L(a,b)\over\sqrt m}      \tag{6.3}
\]

therefore satisfies

\[
                         \Pr(T>t)=e^{-t^2},qquad
                         f_T(t)=2te^{-t^2}.          \tag{6.4}
\]

The shortest half of the paths end at the median
\(t_0=\sqrt{\log2}\).  Since every path has charge capacity two, the
minimum total length of \(N-o(N)\) charged paths is obtained by charging
the shortest half twice.  Therefore

\[
\begin{aligned}
 \min\sum_{\rm charges}L_Q
 &=(2+o(1))N\sqrt m
       \int_0^{t_0}t(2te^{-t^2})\,dt\\
 &=(2+o(1))N\sqrt m
       \left({\sqrt\pi\over2}\operatorname{erf}(t_0)
                    -{t_0\over2}\right)\\
 &=(\kappa+o(1))W,                                  \tag{6.5}
\end{aligned}
\]

where \(N\sqrt m/W\to2/\sqrt\pi\) and \(\kappa\) is (0.2).

When \(H/\sqrt m\to\infty\), truncating every collar at depth \(H\)
does not change (6.5), because the shortest half has length
\((\sqrt{\log2}+o(1))\sqrt m<H\).  Lemma 5.1 proves:

### Theorem 6.1 (endpoint-stitch collision invariant)

Every cycle factor obtained by retaining all product-SCD monotone path
edges and joining their endpoints by cross edges has at least

\[
                         (\kappa+o(1))W              \tag{6.6}
\]

mixed ordered collar occurrences, summed over \(q\le H\) and the two
signs, whose shadow is already occupied by a pure monotone W window.
This remains true if the seam edges are required to be status-cube
orientation edges and regardless of how few cycles the stitching has.

Theorem 6.1 is an exact obstruction to preserving the one-copy W atlas.
It is not by itself a floor-corrected lower bound: at a depth where the
correct target baseline exceeds one, a duplicated canonical target may
be legitimate.  No claim beyond the one-copy ordered ledger is made.

## 7. Exact proved boundary

The full status-cube construction proves the desired owner-side facts:

* exact owner partition;
* full cross-half carrier directions;
* an exponentially small low-dimension leave;
* literal geodesic windows through every \(q\le H\); and
* \(o(W/m)\) cycle components.

It does not prove global lower/upper target simplicity, because a lower
target replaces the touched split pairs by empty pairs and an upper
target replaces them by full pairs.  The target no longer identifies its
source status cell.  This is the precise cross-cell collar ambiguity.

The W atlas supplies canonical target recovery only while a window stays
inside one monotone rectangle path.  Direct endpoint gluing has two exact
obstructions:

1. the cellwise endpoint Hall cuts (3.11), which are not implied by star
   abundance; and
2. even conditional on those cuts, the linear aggregate collision
   invariant (6.6).

Therefore the proposed endpoint reconnection does not yield the claimed
\(o(W)\) ordered-shadow synthesis.  The only surviving use of both
structures is a bulk alternating trade which changes monotone edges on a
positive collar set and proves a new cross-cell target theorem.  Such a
trade is not supplied by either existing construction.
