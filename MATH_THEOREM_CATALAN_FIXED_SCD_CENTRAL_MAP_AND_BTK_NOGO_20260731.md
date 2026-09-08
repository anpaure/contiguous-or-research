# Fixed-SCD central maps: exact criterion and the BTK/GK no-go

Date: 2026-07-31  
Status: all-\(m\) theorem plus deterministic replay for \(2\le m\le10\).
The result closes the *unchanged standard-SCD mate* proposal negatively; it
does not rule out a different SCD or any rethreading of the central mates.

## 1. The central map of an arbitrary SCD

Let \({\cal C}\) be a symmetric-chain decomposition of \(Q_{2m}\).  Every
chain meeting rank \(m-1\) has a unique central segment

\[
        L\ \lessdot\ T\ \lessdot\ U,
        \qquad |L|=m-1,\quad |T|=m,\quad |U|=m+1.       \tag{1.1}
\]

There are

\[
 N=\binom{2m}{m-1}
\]

such chains.  Their \(L\)'s, \(T\)'s and \(U\)'s are separately distinct.
The other middle vertex of the diamond \([L,U]\) is

\[
 H=L\cup(U\setminus T).                               \tag{1.2}
\]

Write \({\cal T}\) for the \(N\) on-chain middle vertices and define the
partial Johnson map

\[
 g_{\cal C}:{\cal T}\longrightarrow\binom{[2m]}m,
 \qquad g_{\cal C}(T)=H.                              \tag{1.3}
\]

The remaining

\[
 \binom{2m}m-N=\operatorname {Cat}_m
\]

middle vertices are precisely the singleton chains of \({\cal C}\).

### Theorem 1.1 (exact fixed-SCD criterion)

Put

\[
 q_{\cal C}(X)=|g_{\cal C}^{-1}(X)|.                  \tag{1.4}
\]

The matching of each rank-\((m-1)\) vertex to its rank-\((m+1)\) mate in
the same SCD chain lifts to the directed Johnson graph

\[
             T\longrightarrow g_{\cal C}(T).
\]

It has middle degree

\[
 \deg(X)={\bf1}_{X\in{\cal T}}+q_{\cal C}(X).         \tag{1.5}
\]

Consequently its lift is a linear forest if and only if

\[
\begin{cases}
q_{\cal C}(X)\le1,&X\in{\cal T},\\
q_{\cal C}(X)\le2,&X\notin{\cal T},
\end{cases}                                           \tag{1.6}
\]

and the partial functional digraph \(T\mapsto g_{\cal C}(T)\) has no
directed cycle.

In particular, injectivity of the alternate-head map \(H\), together with
acyclicity of \(g_{\cal C}\), is sufficient.  It is slightly stronger than
necessary: a singleton middle chain may receive two heads.

#### Proof

Every lifted diamond has endpoints \(T,H\).  The on-chain endpoint occurs
once exactly on \({\cal T}\), while the alternate endpoint occurs
\(q_{\cal C}(X)\) times at \(X\), proving (1.5) and (1.6).

Under (1.6), every component has maximum degree two.  If an undirected
cycle existed, all its vertices would have degree two.  Orienting every
edge from its on-chain endpoint gives outdegree at most one at every
vertex.  The cycle has as many edges as vertices, so every vertex on it
would have outdegree exactly one.  It would therefore be a directed cycle.
The converse is immediate.  \(\square\)

Thus the two requested properties have exact formulations:

* \(H\) is injective iff \(q_{\cal C}(X)\le1\) for every middle \(X\);
* the central map is acyclic iff there are no distinct
  \(T_0,\ldots,T_{s-1}\in{\cal T}\) with
  \(g_{\cal C}(T_i)=T_{i+1}\) cyclically.

A useful sufficient certificate for the second condition is a potential
strictly increasing on every arc.

## 2. The standard BTK/GK map

Fix a coordinate order \(1<2<\cdots<2m\).  In the usual left-to-right
BTK/Greene--Kleitman bracketing, scan a binary word and pair every \(1\)
with the latest still-unpaired \(0\) to its left.  The free positions read
as a block of \(1\)'s followed by a block of \(0\)'s.  Moving upward in a
chain changes the free \(0\)'s to \(1\)'s from left to right.

For a rank-\((m-1)\) word \(L\), let \(a<b\) be its first two free-zero
positions.  Its central diamond is exactly

\[
 T=L+a,\qquad U=L+a+b,\qquad H=L+b.                   \tag{2.1}
\]

### Theorem 2.1 (acyclic but maximally noninjective)

For every \(m\ge2\), the standard BTK/GK central map has the following
properties.

1. It is acyclic.  Indeed, for
   \(\omega(X)=\sum_{i\in X}i\),
   \[
       \omega(H)-\omega(T)=b-a>0.                    \tag{2.2}
   \]
2. Its head map is not injective.  In fact, the middle word
   \[
                X_*=(01)^m                           \tag{2.3}
   \]
   has exactly \(m\) preimages:
   \[
     L_j=(01)^{j-1}00(01)^{m-j},\qquad 1\le j\le m.  \tag{2.4}
   \]
3. The word \(X_*\) is a singleton BTK chain, so its degree in the lifted
   central-mate matching is exactly \(m\).  Hence the unchanged standard
   SCD mate matching violates the degree-two condition for every
   \(m\ge3\).

#### Proof

Equation (2.1) is the definition of the bracketing chain, and (2.2)
proves acyclicity.  In \(L_j\), every \(01\) block outside the displayed
\(00\) is internally paired.  The two zeros in that block are therefore
the first two free zeros.  Adding the second gives \(X_*\), proving (2.4).
All coordinates of \(X_*=(01)^m\) are paired, so its BTK chain is a
singleton.  Formula (1.5) now gives degree \(m\).  \(\square\)

The conclusion is invariant under a permutation of the coordinate order.
Complementing/reversing the standard SCD also complements the same degree
obstruction.  Thus no relabelled or reflected copy of the standard
BTK/GK SCD fixes it.

For \(m=2\), the exceptional degree is only two; (1.6) and (2.2) show that
the fixed-SCD lift is a linear forest even though the prescribed \(H\)-map
is not injective.

## 3. Exact fibre law

The preceding obstruction is not an isolated collision.  It has a closed
distribution.

For a middle word \(X=x_1\cdots x_{2m}\), let

\[
 S_t=|\{i\le t:x_i=0\}|-|\{i\le t:x_i=1\}|,
 \qquad 0\le t\le2m,                                 \tag{3.1}
\]

and let \(\rho(X)\) be the number of visits to the global minimum of
\((S_t)\) *after its first visit*.

### Theorem 3.1 (minimum-return fibre formula)

For the standard BTK/GK central map,

\[
             q(X)=\rho(X).                           \tag{3.2}
\]

Moreover, for every \(0\le j\le m\),

\[
 \boxed{\quad
 |\{X\in\tbinom{[2m]}m:q(X)=j\}|
       =\binom{\,2m-j-1\,}{\,m-j\,}.
 \quad}                                               \tag{3.3}
\]

In particular exactly half of the middle sets are hit:

\[
 |\operatorname {im}H|=\binom{2m-1}{m-1}
     ={1\over2}\binom{2m}m,                          \tag{3.4}
\]

and the unique fibre of size \(m\) is \((01)^m\).

#### Proof

A later return of \(X\) to its global minimum closes one primitive
positive excursion.  Change the final \(1\) of that excursion to \(0\).
The excursion's first \(0\) and this changed position become the first two
free zeros of the resulting rank-\((m-1)\) word; all later excursions pair
internally.  Adding the second free zero recovers \(X\).  Conversely, if
\(L\mapsto X\), the first two free zeros of \(L\) become precisely the
opening and closing positions of such a minimum-level excursion in \(X\).
This is a bijection and proves (3.2).

For completeness, let \(C(z)=1+zC(z)^2\) be the Catalan generating
function.  A balanced word with \(a\) unmatched \(1\)'s and \(a\)
unmatched \(0\)'s (the unmatched positions occur in that order) decomposes
uniquely into \(2a+1\) Dyck words separated by those unmatched symbols.
The central Dyck word is the one at global-minimum level.  A nonempty
primitive Dyck excursion has generating function \(zC(z)\).  Hence the
generating function for words with exactly \(j\) returns to the minimum is

\[
 F_j(z)=(zC(z))^j\sum_{a\ge0}(zC(z)^2)^a
       ={z^jC(z)^{j-1}\over\sqrt{1-4z}}.              \tag{3.5}
\]

The standard coefficient identity

\[
 [z^s]\,{C(z)^a\over\sqrt{1-4z}}=\binom{2s+a}{s}
\]

(valid here also for \(a=-1\)) gives (3.3).  Equations (3.4) and the last
claim follow by taking \(j=0\) and \(j=m\).  \(\square\)

## 4. Consequence for the direct SCD route

The direct proposal

> pair every rank-\((m-1)\) set with its rank-\((m+1)\) mate in one fixed
> standard BTK/GK chain and use that diamond unchanged

is therefore closed negatively for all \(m\ge3\).  Its problem is not
acyclicity--that part has the strongest possible monotone certificate--but
integral head congestion, with a fibre as large as \(m\) and only half the
middle layer used as alternate heads.

This does **not** rule out:

* another, genuinely non-BTK symmetric-chain decomposition;
* changing the lower-to-upper mate matching;
* central rethreading by alternating circuits;
* the decorated-middle-levels two-factor route.

What it does rule out is a recursive proof that simply inherits the
standard BTK/GK central mates without a global rethreading step.

## 5. Replay

Run

    python3 scratch/audit_catalan_btk_central_map_20260731.py

The deterministic replay checks \(m=2,\ldots,10\): injectivity of the
on-chain middle and upper maps, the complete fibre histogram (3.3), the
\(m\)-fold alternating fibre, strict increase of (2.2), absence of directed
cycles, and the induced maximum degree and cap violations.

Artifacts at freeze time:

* script SHA-256:
  0915bd7d399c05f3315be6ee56e8f30028095de82a7c7f0a68bd015abf51722b;
* JSON SHA-256:
  fb177375ae4057374e3ced8249070c3105a2396006cce1ba49d917e315e07363;
* canonical payload SHA-256:
  597d62284e05ed7c9b942641952399a52042f5eb782795fca5ff886f5c1e4015.

