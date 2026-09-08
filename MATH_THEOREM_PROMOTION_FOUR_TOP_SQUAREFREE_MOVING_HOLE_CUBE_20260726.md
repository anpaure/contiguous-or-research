# Promotion rings: a squarefree four-top moving-hole cube with nonzero all-depth floor action

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad H\ge2,
\tag{0.1}
\]

and assume

\[
                         M-2\ge4H.
\tag{0.2}
\]

There is an explicit exchange between four actual one-hole cyclic
frames, one at each of the same four tops, with the following properties.

1. Both shores are squarefree at the middle row.
2. Their complete retained middle-owner vectors are identical.
3. At every lower depth \(1\le q\le H\), the exchange has the nonzero
   four-cell action
   \[
       \Delta_q=-\Gamma_{K_q},\qquad
       \|\Delta_q\|_2^2=4,
   \tag{0.3}
   \]
   where \(K_{q+1}\subset K_q\).
4. At every upper depth \(1\le q<H\), its action is the difference of
   two support-disjoint four-cell rectangles and has squared norm eight;
   at \(q=H\) it is zero. Thus its complete two-sided untagged action is
   \[
                         4H+8(H-1)=12H-8.
   \tag{0.4}
   \]
5. For any floor-corrected collision energy at a lower depth,
   \[
      \Phi_q(\lambda_q+\Delta_q)-\Phi_q(\lambda_q)
       =\langle\lambda_q,\Delta_q\rangle+2.
   \tag{0.5}
   \]
   The two isolated four-frame shores are coordinate-conjugate, so if
   \(R_q\) denotes the ambient load outside the four frames, the same
   change is exactly
   \[
                         \langle R_q,\Delta_q\rangle.
   \tag{0.6}
   \]
   Hence the component has a genuine state-dependent floor choice; it is
   not a load-neutral holonomy.

The construction uses different deleted boundary phases in its two
abstract patterns. This is essential. For a full frame, or for a
common-hole checkerboard cube in any dimension, vanishing middle action
forces vanishing at every lower depth. The present moving-hole cube is
therefore an explicit squarefree primitive outside that rigid
full/common-hole class.

It is an unrestricted physical-frame theorem. No positive-density fixed
mechanical-support embedding, charged coverage theorem, or coefficient-one
conclusion is claimed.

## 1. Two long core runs and four tops

Split an \((M-2)\)-set \(C\) into two disjoint ordered runs

\[
\begin{aligned}
 R&=(z,y_0,y_1,\ldots,y_{r-2}),\qquad |R|=r,\\
 S&=(t_0,t_1,\ldots,t_{s-1}),\qquad |S|=s,
\end{aligned}
\tag{1.1}
\]

where

\[
                         r,s\ge2H,
                         \qquad r+s=M-2.
\tag{1.2}
\]

Choose four distinct labels \(a_0,a_1,b_0,b_1\notin C\), and put

\[
                  U_{ij}=C\cup\{a_i,b_j\}
                  \qquad(i,j\in\{0,1\}).
\tag{1.3}
\]

On the abstract alphabet \(C\cup\{A,B\}\), define the cyclic words

\[
\begin{aligned}
 \alpha&=(A,z,y_0,\ldots,y_{r-2},B,t_0,\ldots,t_{s-1}),\\
 \beta&=(A,y_0,\ldots,y_{r-2},z,B,t_{s-1},\ldots,t_0).
\end{aligned}
\tag{1.4}
\]

Let \(\alpha_{ij},\beta_{ij}\) be their specializations
\(A\mapsto a_i\), \(B\mapsto b_j\).

In \(\alpha\), delete the phase whose middle omitted interval is

\[
                   E_L=(z,y_0,\ldots,y_{H-2}).
\tag{1.5}
\]

In \(\beta\), delete the phase whose middle omitted interval is

\[
                   E_R=(y_{r-H},\ldots,y_{r-2},z).
\tag{1.6}
\]

The deleted phase retains its terminal endpoint at every other depth.
Write \(\alpha_{ij}^-\), \(\beta_{ij}^-\) for these literal one-hole
frames.

The two compound shores are

\[
\begin{aligned}
 \mathcal O&=\{\alpha_{00}^-,\beta_{01}^- ,
                \beta_{10}^-,\alpha_{11}^-\},\\
 \mathcal N&=\{\beta_{00}^-,\alpha_{01}^- ,
                \alpha_{10}^-,\beta_{11}^-\}.
\end{aligned}
\tag{1.7}
\]

Thus every top in (1.3) occurs exactly once on each shore.

For \(h\ge0\), let \(D_h(\gamma_{ij}^-)\) be the retained deck of
targets

\[
                         U_{ij}\setminus Q,
\tag{1.8}
\]

where \(Q\) is the cyclic omitted interval of length \(h\) with the
phase's prescribed terminal endpoint. At \(h=H+q\), these targets have
rank \(M-h=m-q\). Global complementation converts (1.8) into the usual
root-form convention without changing equality, squarefreeness, norms,
or collision energy.

## 2. The alternating cube derivative

For \(K\subseteq C\), define

\[
 \Gamma_K=
 e_{K\cup\{a_0,b_0\}}-e_{K\cup\{a_0,b_1\}}
 -e_{K\cup\{a_1,b_0\}}+e_{K\cup\{a_1,b_1\}}.
\tag{2.1}
\]

Then

\[
                         \|\Gamma_K\|_2^2=4,
\tag{2.2}
\]

and \(\Gamma_K,\Gamma_{K'}\) have disjoint supports when \(K\ne K'\).

Let \(\mathcal Q_h^-(\gamma)\) be the retained length-\(h\) omitted
intervals of the abstract punctured word \(\gamma\) which contain
neither \(A\) nor \(B\).

### Lemma 2.1 (punctured cube derivative)

For \(\gamma\in\{\alpha,\beta\}\),

\[
 \sum_{i,j}(-1)^{i+j}D_h(\gamma_{ij}^-)
 =\sum_{Q\in\mathcal Q_h^-(\gamma)}\Gamma_{C\setminus Q}.
\tag{2.3}
\]

#### Proof

If the omitted interval \(Q\) contains \(A\), then its complementary
target is independent of \(i\), and the alternating sum over \(i\)
vanishes. The same applies to \(B\) and \(j\). If \(Q\subset C\), its
four specialized complementary targets are

\[
       (C\setminus Q)\cup\{a_i,b_j\},
\]

whose alternating sum is precisely \(\Gamma_{C\setminus Q}\).
Summing the retained phases proves (2.3). \(\square\)

The load change \(\mathcal N-\mathcal O\) at complementary length \(h\)
is therefore

\[
 \Delta_h=
 \sum_{Q\in\mathcal Q_h^-(\beta)}\Gamma_{C\setminus Q}
 -\sum_{Q\in\mathcal Q_h^-(\alpha)}\Gamma_{C\setminus Q}.
\tag{2.4}
\]

## 3. Exact middle equality and squarefreeness

### Theorem 3.1 (literal middle-owner legality)

The two shores in (1.7) have identical retained middle-owner vectors,
and this common vector is squarefree.

#### Proof: equality

The placeholders split each word into the two core runs \(R,S\). In
\(R\), the length-\(H\) core intervals of \(\alpha\) consist of the
left exceptional interval \(E_L\), the common internal \(y\)-intervals,
and no right exceptional interval. Those of \(\beta\) consist of the
same internal intervals and the right exceptional interval \(E_R\).
Deleting (1.5)--(1.6) leaves exactly the same internal family.

The \(S\)-run is reversed between \(\alpha\) and \(\beta\); reversal
does not change the family of its unordered length-\(H\) intervals.
Consequently

\[
                   \mathcal Q_H^-(\alpha)
                   =\mathcal Q_H^-(\beta).
\tag{3.1}
\]

Equations (2.4) and (3.1) give \(\Delta_H=0\).

#### Proof: squarefreeness

Within one frame, distinct proper cyclic intervals give distinct target
sets. Consider two different tops on the same shore.

If their indices differ in both coordinates, equality of two targets
would require the two omitted \(H\)-intervals to contain both \(A\) and
\(B\). This is impossible: the two cyclic gaps between the placeholders
contain \(r\) and \(s\) core labels, respectively, and both are at least
\(2H\).

Suppose the tops differ only in the \(a\)-coordinate. Their patterns are
one \(\alpha\) and one \(\beta\). Equality of targets would require
omitted intervals containing \(A\) whose \((H-1)\)-element core traces
are equal. Such a trace uses some number \(p\) of labels from the
\(S\)-side of \(A\) and \(H-1-p\) labels from its \(R\)-side.
Equality forces the same \(p\), since \(R\cap S=\varnothing\).

For \(p>0\), the \(\alpha\)-trace uses the last \(p\) labels of
\((t_0,\ldots,t_{s-1})\), whereas the \(\beta\)-trace uses the first
\(p\). These sets are disjoint because \(p\le H-1\) and \(s\ge2H\).
For \(p=0\), the two \(R\)-parts are

\[
 \{z,y_0,\ldots,y_{H-3}\},\qquad
 \{y_0,\ldots,y_{H-2}\},
\tag{3.2}
\]

and are different. Thus no collision is possible.

The case of two tops differing only in the \(b\)-coordinate is the same
at the other ends of the runs. If the trace uses a nonzero number of
\(S\)-labels, it compares an initial and a terminal segment of the long
\(S\)-run. If it uses only \(R\)-labels, it compares

\[
 \{y_{r-H},\ldots,y_{r-2}\},\qquad
 \{y_{r-H+1},\ldots,y_{r-2},z\},
\tag{3.3}
\]

which are different. Hence no two frames on either shore share a middle
target. Together with \(\Delta_H=0\), this proves the theorem. \(\square\)

Because the middle vectors are literally equal, replacing \(\mathcal O\)
by \(\mathcal N\) inside any squarefree global middle resolution preserves
all middle ownership, including collisions with untouched frames.

## 4. Exact lower and upper action

### Theorem 4.1 (nested lower rectangles)

For \(1\le q\le H\), put \(h=H+q\) and

\[
 Q_q^L=\{z,y_0,\ldots,y_{h-2}\},
 \qquad K_q=C\setminus Q_q^L.
\tag{4.1}
\]

Then

\[
                         \Delta_{H+q}=-\Gamma_{K_q},
                         \qquad\|\Delta_{H+q}\|_2^2=4,
\tag{4.2}
\]

and

\[
                         K_{q+1}=K_q\setminus\{y_{H+q-1}\}.
\tag{4.3}
\]

#### Proof

The core length-\(h\) intervals in the reversed \(S\)-runs agree as
set families. In \(R\), the two full families have the same internal
\(y\)-intervals; \(\alpha\) has the exceptional left interval \(Q_q^L\),
while \(\beta\) has the exceptional right interval ending in \(z\).

The deleted \(\alpha\)-phase has terminal endpoint \(y_{H-2}\). At
length \(H+q\), its omitted interval extends across \(A\), so it deletes
no core-only interval. The deleted \(\beta\)-phase has terminal endpoint
\(z\) and deletes its exceptional right core interval. Therefore

\[
 \mathcal Q_h^-(\beta)-\mathcal Q_h^-(\alpha)=-Q_q^L
\]

as a signed family. Equation (2.4) proves (4.2), and (4.1) gives
(4.3). \(\square\)

### Proposition 4.2 (upper rectangles)

For \(1\le q<H\), put \(h=H-q\) and

\[
\begin{aligned}
 Q_q^L&=\{z,y_0,\ldots,y_{h-2}\},\\
 Q_q^D&=\{y_{q-1},\ldots,y_{H-2}\},\\
 K_q^L&=C\setminus Q_q^L,\qquad
 K_q^D=C\setminus Q_q^D.
\end{aligned}
\tag{4.4}
\]

Then

\[
 \Delta_{H-q}=\Gamma_{K_q^D}-\Gamma_{K_q^L},
 \qquad \|\Delta_{H-q}\|_2^2=8.
\tag{4.5}
\]

At \(q=H\), the action is zero.

#### Proof

Before puncturing, the \(R\)-families differ by right exceptional minus
left exceptional. At length \(h\), the \(\alpha\)-hole deletes the
internal interval \(Q_q^D\), while the \(\beta\)-hole deletes the right
exceptional interval. Hence the retained \(\beta\)-family minus the
retained \(\alpha\)-family is \(Q_q^D-Q_q^L\). The \(S\)-families still
cancel. Equation (2.4) proves (4.5). The two \(Q\)'s are distinct because
exactly one contains \(z\), so their \(\Gamma\)-supports are disjoint.
At \(h=0\), every phase target is its full top and is independent of the
pattern and hole, giving zero action. \(\square\)

Equations (4.2) and (4.5) prove the action total (0.4). They are literal
untagged row identities. An arbitrary preassigned phase-to-depth tag
schedule need not retain all their terms and is not claimed here.

## 5. Exact floor derivative

At a fixed row let \(\lambda\) be the ambient integer load before the
exchange and let \(\Delta\) be its load change. Every shore has the same
number of occurrences, so \(\sum_T\Delta_T=0\). For

\[
                         \operatorname{Col}(\lambda)
                         =\sum_T\binom{\lambda_T}{2},
\tag{5.1}
\]

one has the exact identity

\[
 \operatorname{Col}(\lambda+\Delta)-
 \operatorname{Col}(\lambda)
 =\langle\lambda,\Delta\rangle+rac12\|\Delta\|_2^2.
\tag{5.2}
\]

Every rankwise floor correction is constant on the fixed-total affine
slice, so (5.2) is also the exact floor-corrected change. At a lower
depth, (4.2) gives (0.5); at an upper depth, (4.5) gives

\[
                         \langle\lambda,\Delta\rangle+4.
\tag{5.3}
\]

The coordinate transposition \((a_0\ a_1)\) maps \(\mathcal O\) to
\(\mathcal N\), including their holes. Hence their isolated load vectors
have equal collision energy at every row. Writing

\[
                         \lambda=L_{\mathcal O}+R
\tag{5.4}
\]

in (5.2), the isolated packet contribution cancels and leaves

\[
 \Phi(L_{\mathcal N}+R)-\Phi(L_{\mathcal O}+R)
                         =\langle R,\Delta\rangle.
\tag{5.5}
\]

Thus the two legal middle-owner resolutions expose an exact nonzero
floor direction to the external load. Reversing the shore choice reverses
the sign. A strict descent occurs whenever the current shore is the
higher of the two; equality is the only flat case.

## 6. Rigidity boundary

If no pattern-dependent phase is deleted, the alternating cube derivative
at complementary length \(h\) is

\[
 \sum_{Q\in\mathcal Q_h(\gamma)}\Gamma_{C\setminus Q},
\tag{6.1}
\]

where \(\mathcal Q_h(\gamma)\) is the family of core-only \(h\)-windows.
The vectors \(\Gamma_K\) have disjoint supports. Therefore zero middle
action forces equality of the two core \(H\)-window families.

Those families reconstruct each core run: their intersection-
\((H-1)\) graph is the disjoint union of the paths of consecutive
\(H\)-windows. Every longer core window is the union of a consecutive
block of path vertices. Hence equality at length \(H\) forces equality
at every length \(h\ge H\). The same proof applies to a common deleted
phase whose alternating contribution vanishes.

Thus every full or common-hole common-base checkerboard cube, including
all four- and eight-top variants and arbitrary mixed positional patterns,
is lower-depth load-neutral whenever it is middle-neutral. The unequal
moving holes (1.5)--(1.6) are exactly what escapes this no-go.

## 7. Exact boundary

Proved:

1. a four-top exchange of literal one-hole cyclic frames;
2. squarefree old and new middle shores with exactly the same owner set;
3. a nested nonzero four-cell transfer at every lower depth;
4. explicit nonzero upper action and exact total action \(12H-8\);
5. the exact floor derivative, with no hidden raw-Gram substitution; and
6. the full/common-hole cube rigidity explaining why the moving phase is
   necessary.

Not proved:

1. that a positive-density family of these components can be packed
   owner-disjointly;
2. that their external charges admit a simultaneously favorable choice
   through all depths;
3. compatibility with an arbitrary fixed tag schedule or fixed
   mechanical atlas; or
4. coefficient one.

The next exact gate is a charged squarefree-component theorem: pack these
four-top seams so that the linked external correlations in (5.5) have a
negative total, while retaining the nested tag census.
