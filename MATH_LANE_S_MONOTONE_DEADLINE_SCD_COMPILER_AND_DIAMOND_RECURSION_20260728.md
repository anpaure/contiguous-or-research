# Lane S: monotone-deadline SCD allocation, physical pin obstruction, and the exact diamond recursion gate

Date: 2026-07-28

Method: pure mathematics only. No web search, finite search, solver, or
computational experiment is used in this note. The stored exact words for
\(k=11,12,13,14\) are used only as already certified finite inputs; the
claims extracted from them below are direct endpoint and carrier audits.

## 0. Outcome

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},
\]

and let \(d=d(k)\) be least such that

\[
 \Lambda\le dW+t_d,
 \qquad t_d:=\binom{d+1}{2}.
\tag{0.1}
\]

Write

\[
 B(k)=W+d,
 \qquad
 \sigma=dW+t_d-\Lambda.
\tag{0.2}
\]

The monotone-deadline theorem gives \(\nu(k)\ge B(k)\). This note asks
whether a full symmetric-chain decomposition can turn the equality
structure, and the exact \(k=11,12,13,14\) words, into an all-\(k\)
optimal carrier/compiler or a \(k\mapsto k+2\) recursion.

The answer splits sharply into a positive abstract theorem and two exact
physical obstructions.

1. **All-\(k\) integral SCD allocation.** Give every middle owner \(d\)
   labelled slots and add the \(t_d\) triangular tail slots. Every nonempty
   strict-lower set can be integrally assigned to a slot of a containing
   middle owner or to the tail. This follows from one exact containment
   Hall inequality and is valid for every \(k\).

2. **The allocation is not a literal OR compiler.** Minimum-length
   residence runs force individual coordinates to unique physical ports.
   A target can be contained in a middle owner while being forbidden from
   all \(d\) short cells nominally belonging to that owner. The exact
   \(k=14\) word realizes this obstruction at equality.

3. **Every SCD has a bulk local-load obstruction.** If a lower target is
   kept in its native SCD chain except at tail or seam cells, the exact
   unavoidable export is

   \[
    E_{k,d}=\sum_{j=d+1}^{r-1}\binom{k}{r-j}.
   \]

   After the tail is used, the exact exports for \(k=11,12,13,14\) are
   \(60,295,371,1467\). Asymptotically
   \(E_{k,d}=\Theta(W\sqrt{k})\). Hence the exact words necessarily use
   bulk global pin rematching, not an SCD-chain-local compiler.

4. **Exact same-parity scalar recursion.** For both parities,
   \(d(k+2)\in\{d(k),d(k)+1\}\), with an exact Catalan/slack criterion.
   The criterion explains the finished transitions \(11\to13\) and
   \(12\to14\), and gives \(d(16)=3\).

5. **A genuine central carrier recursion.** From an odd-dimensional cyclic
   carrier with complete first lower and first upper shadows, one obtains
   explicitly a Hamilton cycle through the entire \((k+2)\)-dimensional
   middle deck. This is a positive, integral central-ownership theorem.

6. **The natural diamond chronology is not a compiler.** Its two new
   coordinates have runs of length two; it has no \(AA\) edges and no
   \(UU\) edges. Thus for every relevant deadline \(d'\ge2\) it fails
   residence and simultaneously misses an entire both-new lower family and
   an entire empty-signature upper family. These defects cannot be repaired
   by the lower Hall matching.

7. **The exact surviving recursion gate is colored and all-depth.** The
   \(A\)-sector requires a one-representative-per-color forest avoiding
   every residence-hazard interval. The \(U\)-sector requires a
   one-representative-per-color vertex cover of the old index cycle and,
   at every deeper upper target, a wholly retained provider interval. The
   locally perfect \(J(4,2)\) rectangle cannot mix these choices: exact
   use of every cross state forces constant phase on each old carrier
   cycle.

Consequently no all-\(k\) optimal compiler or unconditional
\(k\mapsto k+2\) recurrence is proved here. What is proved is stronger
than a layerwise Hall reduction: the natural SCD-local and edge-local
recursions are rigorously closed, an exact central Hamilton recursion is
constructed, and the remaining nonlocal braid/pin problem is stated with
residence and every upper shadow included.

## 1. Flat equality and its exact endpoint geometry

Let \(A=(A_0,\ldots,A_{L-1})\) be a nonzero word of length

\[
 L=W+d
\]

and suppose its depth-\(d\) row

\[
 T_i=(D^dA)_i=\bigcup_{p=i}^{i+d}A_p,
 \qquad 0\le i<W,
\tag{1.1}
\]

is a permutation of \(\binom{[k]}r\). For \(0\le s<d\), call

\[
 C_{s,j}:=(D^sA)_j=\bigcup_{p=j}^{j+s}A_p,
 \qquad 0\le j<L-s,
\tag{1.2}
\]

a short-band cell.

### Lemma 1.1 (all depth loss is on the two boundary chains)

If

\[
 1\le j\le L-s-2,
\]

then \(C_{s,j}\) is contained in at least two distinct central windows
\(T_i\). Consequently

\[
 |C_{s,j}|\le r-1.
\tag{1.3}
\]

#### Proof

The central intervals containing \([j,j+s]\) are those \([i,i+d]\)
with

\[
 j+s-d\le i\le j,
 \qquad 0\le i<W.
\]

Because \(s<d\), an interior short interval has at least two such starts.
Thus \(C_{s,j}\subseteq T_i\cap T_{i'}\) for distinct \(i,i'\). If
\(|C_{s,j}|=r\), then containment between three rank-\(r\) sets would give
\(C_{s,j}=T_i=T_{i'}\), contradicting the fact that the central row is a
permutation. Therefore \(|C_{s,j}|\le r-1\). \(\square\)

Define the nested boundary chains

\[
 L_s=C_{s,0},
 \qquad
 R_s=C_{s,L-s-1},
 \qquad 0\le s\le d,
\]

and let

\[
 a_L=\min\{s:|L_s|=r\},
 \qquad
 a_R=\min\{s:|R_s|=r\}.
\tag{1.4}
\]

These values lie in \(\{0,\ldots,d\}\), because \(L_d=T_0\) and
\(R_d=T_{W-1}\).

### Theorem 1.2 (exact endpoint-loss formula)

Let \(\Delta_{\rm depth}\) be the difference between the maximum short-band
cell count \(dW+t_d\) and the actual number of lower-rank cells. Let
\(\Delta_{\rm repeat}\) be the lower-cell occurrence count minus
\(\Lambda\). Then

\[
 \boxed{\Delta_{\rm depth}=2d-a_L-a_R},
 \qquad
 \boxed{\Delta_{\rm repeat}=\sigma-\Delta_{\rm depth}}.
\tag{1.5}
\]

In particular,

\[
 0\le\Delta_{\rm depth}\le2d.
\tag{1.6}
\]

#### Proof

By Lemma 1.1 every nonboundary cell in rows \(0,\ldots,d-1\) is lower.
The number of such cells is

\[
 \sum_{s=0}^{d-1}(L-s-2)=dW+t_d-2d.
\]

The left boundary contributes exactly \(a_L\) lower cells and the right
boundary exactly \(a_R\). Hence the actual lower-cell count is

\[
 dW+t_d-2d+a_L+a_R,
\]

which proves the first identity. The monotone-deadline equality ledger is

\[
 \sigma=\Delta_{\rm depth}+\Delta_{\rm repeat};
\]

the second identity follows. \(\square\)

### Exact audit of the stored \(k=11,12,13,14\) words

Directly following the two endpoint chains in the stored flat
representatives gives

\[
\begin{array}{c|c|c|c|c}
k&d& (a_L,a_R)&\Delta_{\rm depth}&\Delta_{\rm repeat}\\ \hline
11&3&(3,3)&0&369\\
12&2&(1,1)&2&264\\
13&3&(3,1)&2&1057\\
14&2&(2,1)\text{ up to reversal}&1&391.
\end{array}
\tag{1.7}
\]

Thus positive slack in the known words is overwhelmingly repeated lower
mass, not unused interior capacity. The earlier possible inference that
all four words saturate every lower-depth cell is false: the \(k=12\)
words have two rank-six cells in \(D^1\), while the \(k=14\) word has one
rank-seven cell in \(D^1\).

There is an immediate recursion consequence. Concatenating four depth-\(d\)
bands into one deletes three seam triangles, totaling \(3t_d\) cells.
The parent endpoint chains supply at most \(2d\) automatically nonlower
cells. For growing \(d\), the \(O(d)\) endpoint loss cannot pay the
\(\Theta(d^2)\) seam deletion. A recursion must deliberately rematch
repeated lower occurrences so that the three deleted triangles carry no
unique targets. Literal copying of the parent words is therefore already
excluded by (1.5).

## 2. An all-\(k\) integral SCD/containment allocation

Create \(d\) distinguishable slots

\[
 (X,h),\qquad X\in\binom{[k]}r,quad 1\le h\le d,
\]

and \(t_d\) additional universal tail slots. Join a nonempty strict-lower
target \(S\) to every \((X,h)\) with \(S\subseteq X\), and to every tail
slot.

### Theorem 2.1 (integral containment allocation)

For every \(k\), this bipartite graph has a matching saturating all
nonempty strict-lower targets.

#### Proof

Let \(\mathcal A\) be a nonempty family of lower targets, write

\[
 \mathcal A_s=\mathcal A\cap\binom{[k]}s,
\]

and let \(N(\mathcal A)\) be the family of middle \(r\)-sets containing
at least one member of \(\mathcal A\). Counting incidences
\((S,X)\) with \(S\in\mathcal A_s\) and \(S\subseteq X\) gives

\[
 |\mathcal A_s|\binom{k-s}{r-s}
 \le |N(\mathcal A)|\binom{r}{s}.
\]

Using

\[
 \binom{k}{s}\binom{k-s}{r-s}
 =W\binom{r}{s},
\]

we obtain

\[
 |\mathcal A_s|
 \le \frac{\binom{k}{s}}{W}|N(\mathcal A)|.
\]

Summing over \(1\le s<r\),

\[
 |\mathcal A|
 \le\frac{\Lambda}{W}|N(\mathcal A)|
 \le d|N(\mathcal A)|+t_d\frac{|N(\mathcal A)|}{W}
 \le d|N(\mathcal A)|+t_d.
\tag{2.1}
\]

The right side is exactly the size of the slot neighborhood of
\(\mathcal A\). Hall's theorem gives the required integral matching.
\(\square\)

This theorem is the strongest purely layerwise consequence of the SCD
census: it is simultaneous over every lower rank and has no fractional
rounding. It deliberately does **not** say that a slot of a containing
middle owner is a physical interval capable of realizing the assigned set.
Section 4 shows that this missing implication is false.

## 3. The exact SCD-local overload

Fix any full symmetric-chain decomposition of \(2^{[k]}\). Every chain
contains one rank-\(r\) middle owner. Let \(h(C)\) be the number of its
nonempty members strictly below rank \(r\).

### Theorem 3.1 (universal SCD overload formula)

The amount by which the native lower members exceed \(d\) private slots per
chain is

\[
 \boxed{
 E_{k,d}:=\sum_C(h(C)-d)_+
 =\sum_{j=d+1}^{r-1}\binom{k}{r-j}.}
\tag{3.1}
\]

Consequently, even after all \(t_d\) universal tail cells are used, a
compiler which otherwise keeps every lower target in its own SCD chain must
export at least

\[
 E_{k,d}-t_d
\tag{3.2}
\]

targets.

#### Proof

The number of SCD chains beginning at rank \(s\) is

\[
 c_s=\binom{k}{s}-\binom{k}{s-1}.
\]

For \(1\le j\le r-1\), a chain has at least \(j\) nonempty strict-lower
members exactly when it begins at rank at most \(r-j\). Therefore

\[
 \#\{C:h(C)\ge j\}
 =\sum_{s=0}^{r-j}
 \left(\binom{k}{s}-\binom{k}{s-1}\right)
 =\binom{k}{r-j}.
\]

Now use the layer-cake identity

\[
 \sum_C(h(C)-d)_+
 =\sum_{j=d+1}^{r-1}\#\{C:h(C)\ge j\}.
\]

This proves (3.1). At most \(t_d\) exported targets can occupy the tail,
which proves (3.2). \(\square\)

For the exact dimensions,

\[
\begin{array}{c|c|c|c}
k&d&E_{k,d}&E_{k,d}-t_d\\ \hline
11&3&66&60\\
12&2&298&295\\
13&3&377&371\\
14&2&1470&1467.
\end{array}
\tag{3.3}
\]

These numbers are much larger than the number of carrier seams in the
exact words: \(k=11\) uses one cyclic carrier, \(k=13\) uses two cycles
and one shadow-safe splice, and \(k=14\) uses a six-piece braid. Hence
those words cannot be interpreted as chain-local SCD compilers. Their lower
pins are globally rematched through the interiors of the physical bands.

There is also an exact seam-local strengthening. A fixed cut is crossed by

\[
 \sum_{s=1}^{d-1}s=\binom d2
\tag{3.4}
\]

short-band intervals. If every off-chain target must lie either in a tail
cell or in a cell crossing one of \(z\) seams, then necessarily

\[
 \boxed{z\binom d2+t_d\ge E_{k,d}.}
\tag{3.5}
\]

For \(k=11,12,13,14\), this forces respectively

\[
 z\ge20,\quad295,\quad124,\quad1467.
\tag{3.6}
\]

Thus not even a bounded-seam refinement of the native SCD assignment can
explain the finite optimal words.

Finally, the obstruction is asymptotically macroscopic. The local central
limit estimates give

\[
 \frac d{\sqrt{k}}\longrightarrow
 \alpha:=\sqrt{\frac\pi8}
 =\int_0^\infty e^{-2x^2}\,dx,
\]

and, uniformly for \(j=O(\sqrt{k})\),

\[
 \frac{\binom{k}{r-j}}{W}
 =e^{-2j^2/k+o(1)}.
\]

Therefore

\[
 \boxed{
 \frac{E_{k,d}}{W\sqrt{k}}
 \longrightarrow
 \beta:=\int_\alpha^\infty e^{-2x^2}\,dx>0.}
\tag{3.7}
\]

In particular a seam-local recursion would need

\[
 z\ge
 \left(\frac{2\beta}{\alpha^2}+o(1)\right)
 \frac{W}{\sqrt{k}},
\tag{3.8}
\]

which is the full residence-compatible seam scale rather than a bounded
number of repairs.

## 4. Why containment Hall is not a literal lower compiler

Let \(T=(T_0,\ldots,T_{W-1})\) be a flat central chronology at depth
\(d\). For a coordinate \(x\), suppose its central trace has a maximal
internal one-run \([a,b]\):

\[
 x\in T_a,\ldots,T_b,
 \qquad x\notin T_{a-1},T_{b+1}.
\]

### Lemma 4.1 (exact residence-with-pins law)

The only physical positions at which \(x\) may occur are

\[
 [a+d,b].
\tag{4.1}
\]

After all lower equalities have forbidden positions, let \(Q_x\) be the
remaining legal set. There exists an \(x\)-support realizing this run if
and only if

1. \(a+d,b\in Q_x\); and
2. consecutive points of \(Q_x\cap[a+d,b]\) have distance at most
   \(d+1\).

#### Proof

A physical occurrence at position \(p\) enters exactly the central windows
with starts in \([p-d,p]\). Requiring all such starts to lie in \([a,b]\)
is equivalent to \(a+d\le p\le b\), proving (4.1). The leftmost positive
window \([a,a+d]\) meets (4.1) only at \(a+d\), and the rightmost positive
window \([b,b+d]\) meets it only at \(b\); both endpoints are forced. A
gap of at least \(d+2\) leaves a central window unhit, while gaps at most
\(d+1\) hit every intervening central window. This is necessary and
sufficient. \(\square\)

Boundary runs have the analogous one-sided rule: the interior endpoint is
forced and all gaps are at most \(d+1\).

### Corollary 4.2 (minimum-run physical obstruction)

If \(b-a+1=d+1\), then \(x\) is forced at the unique position

\[
 p=a+d=b.
\]

In particular, although \(x\in T_a\), none of the nominal owner cells

\[
 [a,a+s],\qquad0\le s<d,
\tag{4.2}
\]

contains \(x\). Hence no target containing \(x\) can be placed in these
cells.

This is an exact counterexample to the implication

\[
 S\subseteq T_a
 \quad\Longrightarrow\quad
 \text{one of the \(d\) short cells of owner \(T_a\) can realize \(S\)}.
\]

The obstruction is not hypothetical: in the exact \(k=14\) word, at
deadline \(d=2\), the inserted coordinate has an internal run of length
three and therefore a unique forced physical port.

For a complete physical compiler, choose an injective assignment \(\phi\)
of every lower target \(S\) to a short physical interval \(I_S\), and set

\[
 Q_x=[0,L-1]\setminus
 \left(
  \bigcup_{i:x\notin T_i}[i,i+d]
  \ \cup\!
  \bigcup_{S:x\notin S}I_S
 \right).
\tag{4.3}
\]

The simultaneous coordinate conditions are:

\[
 [i,i+d]\cap Q_x\ne\varnothing
 \quad(x\in T_i),
\tag{F1}
\]

\[
 I_S\cap Q_x\ne\varnothing
 \quad(x\in S),
\tag{F2}
\]

\[
 \bigcup_xQ_x=[0,L-1].
\tag{F3}
\]

The maximal literal word is then

\[
 A_p=\{x:p\in Q_x\}.
\tag{4.4}
\]

Theorem 2.1 supplies only an unlabelled containment matching; it supplies
none of (F1)--(F3). This distinction is decisive. An audited \(k=13\)
carrier exists with perfect unlabelled target-to-locally-feasible-cell
matching and no zero-candidate target, yet its simultaneous coordinate
compiler is infeasible. Thus no rankwise or ordinary Hall argument may be
used as a substitute for (F1)--(F3).

## 5. Exact same-parity deadline recursion

Let \(k+2\) have middle width \(W'\), lower census \(\Lambda'\), deadline
\(d'\), and slack \(\sigma'\). Put

\[
 c=C_r=\frac1{r+1}\binom{2r}{r},
\]

and let \(\varepsilon=0\) when \(k\) is odd and \(\varepsilon=1\) when
\(k\) is even.

### Theorem 5.1 (exact \(k\mapsto k+2\) scalar recurrence)

For every \(r\ge2\),

\[
 \boxed{W'=4W-(1+\varepsilon)c},
 \qquad
 \boxed{\Lambda'=4\Lambda+\varepsilon c+3}.
\tag{5.1}
\]

Moreover,

\[
 \boxed{d'\in\{d,d+1\}}.
\tag{5.2}
\]

Define

\[
 \boxed{
 G=\bigl[d+\varepsilon(d+1)\bigr]c+3t_d+3.}
\tag{5.3}
\]

Then

\[
 \boxed{
 \begin{array}{ll}
 4\sigma\ge G:
 &d'=d,\qquad \sigma'=4\sigma-G,\\[1mm]
 4\sigma<G:
 &d'=d+1,\qquad
 \sigma'=4\sigma-G+W'+d+1.
 \end{array}}
\tag{5.4}
\]

#### Proof

Pascal expansion gives

\[
 \Lambda'
 =4\Lambda+W-\binom{k}{r-1}+3.
\tag{5.5}
\]

For odd \(k=2r-1\), the correction vanishes; for even \(k=2r\), it is
\(c\). The central binomial identities similarly give the formula for
\(W'\).

Old minimality says

\[
 (d-1)W+t_{d-1}<\Lambda.
\]

Since \(W'<4W\) and \(t_{d-1}<4t_{d-1}\),

\[
 (d-1)W'+t_{d-1}<4\Lambda<\Lambda',
\]

so \(d'\ge d\).

For the upper bound, \(d\le r-1\). In the odd case the required
difference

\[
 (d+1)W'+t_{d+1}-(4dW+4t_d+3)
\]

is decreasing in \(d\), and at \(d=r-1\) is nonnegative by
\(W\ge\binom{r+2}{3}\). In the even case the corresponding difference is

\[
 S(d)=4W-(2d+3)c+\frac{(d+1)(2-3d)}2-3.
\]

It too decreases for \(d\le r-1\); at \(d=r-1\), using
\(c=W/(r+1)\) and \(W\ge r^2\),

\[
 S(r-1)>
 2W+\frac{r(5-3r)}2-3
 \ge\frac{(r+6)(r-1)}2\ge0.
\]

Thus \(d'\le d+1\).

Finally, substitution of (5.1) into the slack at unchanged depth gives

\[
 dW'+t_d-\Lambda'=4\sigma-G.
\]

Its sign decides whether depth \(d\) works. Raising the depth adds exactly
\(W'+d+1\) cells, proving (5.4). \(\square\)

The exact calibrations are

\[
\begin{array}{c|c|c|c|c|c}
k&d&\sigma&c&G&\text{target}\\ \hline
11&3&369&132&417&d(13)=3,\ \sigma_{13}=1059\\
12&2&266&132&672&d(14)=2,\ \sigma_{14}=392\\
13&3&1059&429&1308&d(15)=3,\ \sigma_{15}=2928\\
14&2&392&429&2157&d(16)=3,\ \sigma_{16}=12284.
\end{array}
\tag{5.6}
\]

When the deadline is retained, \(G\) is the exact number of source holes
which must disappear: contraction removes
\(d(1+\varepsilon)c+3t_d\) source cells, while the child lower family has
\(\varepsilon c+3\) labels beyond four source copies. This is scalar
arithmetic, not a physical rule for choosing the disappearing holes.

## 6. Status census and the sector-local capacity wall

Adjoin coordinates \(x,y\). The child middle layer has four status sectors

\[
\begin{array}{c|c}
\text{status}&\text{number of middle states}\\ \hline
\varnothing&\binom{k}{r+1}=W-c\\
\{x\}&W\\
\{y\}&W\\
\{x,y\}&\binom{k}{r-1}.
\end{array}
\tag{6.1}
\]

The strict-lower target counts are

\[
\begin{array}{c|c}
\text{status}&\text{number of targets}\\ \hline
\varnothing&\Lambda+W\\
\{x\}&\Lambda+1\\
\{y\}&\Lambda+1\\
\{x,y\}&\Lambda-\binom{k}{r-1}+1.
\end{array}
\tag{6.2}
\]

### Theorem 6.1 (empty-status sector deficiency)

Even if the empty-status sector receives its own isolated depth-\(d'\)
band and all \(t_{d'}\) triangular boundary cells, its exact lower
deficiency is

\[
 \boxed{
 \Delta_0=\Lambda+W-
 \left[d'(W-c)+t_{d'}\right]>0.}
\tag{6.3}
\]

If \(d'=d\), then

\[
 \Delta_0=W+dc-\sigma
 \ge d(c-1)+1.
\tag{6.4}
\]

If \(d'=d+1\), then

\[
 \Delta_0=(d+1)c-d-1-\sigma>0.
\tag{6.5}
\]

#### Proof

Only the displayed number of physical short cells is available in an
isolated band, proving the formula. If \(d'=d\), old minimality implies
\(\sigma\le W+d-1\), giving (6.4). If \(d'=d+1\), use the jump inequality
\(4\sigma<G\). In the worse even-parity case,

\[
 4(d+1)(c-1)-G
 =(2d+3)c-3t_d-4d-7>0,
\]

where \(c\ge d+3\); the odd case is easier. Integrality gives (6.5).
\(\square\)

For source dimensions \(11,12,13,14\),

\[
 \Delta_0=489,\quad922,\quad1944,\quad892.
\tag{6.6}
\]

Thus four independent status compilers fail even before coordinate pins are
considered. At a no-jump step the deficiency is
\(\Theta(dc)=\Theta(W/\sqrt{k})\), so bounded seam repair is impossible.
The child compiler must use genuinely cross-status physical cells.

## 7. A positive exact central Hamilton recursion

We now construct the strongest unconditional part of the diamond lift.
Let \(k=2r-1\), let

\[
 T_0,T_1,\ldots,T_{W-1}
\]

be a cyclic Hamilton ordering of the old rank-\(r\) layer, with indices
modulo \(W\), and assume

\[
 C_i:=T_i\cap T_{i+1}
\]

enumerates every rank-\((r-1)\) set exactly once. Assume also that

\[
 V_i:=T_i\cup T_{i+1}
\]

covers every rank-\((r+1)\) set. Choose one occurrence index of each
distinct \(V\)-color and call the selected set \(I\). Then

\[
 |I|=\binom{2r-1}{r+1}=W-c.
\]

Define child rank-\((r+1)\) states

\[
 Y_i=T_i\cup\{y\},
 \qquad
 A_i=C_i\cup\{x,y\},
 \qquad
 X_i=T_{i+1}\cup\{x\},
\tag{7.1}
\]

and, for \(i\in I\),

\[
 U_i=V_i.
\tag{7.2}
\]

### Theorem 7.1 (compressed diamond Hamilton cycle)

The cyclic block word

\[
 \prod_{i\in\mathbb Z_W}
 \bigl([U_i\text{ if }i\in I],Y_i,A_i,X_i\bigr)
\tag{7.3}
\]

is a Hamilton cycle of the entire child middle layer
\(\binom{[k]\cup\{x,y\}}{r+1}\).

#### Proof

The four families are disjoint by new-coordinate status. The \(X\),
\(Y\), and \(A\) families each have \(W\) states, and the \(U\) family
has \(W-c\). They enumerate their corresponding sectors because the
\(T_i\), \(C_i\), and selected \(V_i\) enumerate the required old
layers.

Every displayed transition is Johnson. Indeed,

\[
 Y_i\cap A_i=C_i\cup\{y\},
 \qquad
 A_i\cap X_i=C_i\cup\{x\},
\]

both of size \(r\). If \(U_i\) is absent, then

\[
 X_{i-1}\cap Y_i=T_i;
\]

if \(U_i\) is present, then

\[
 X_{i-1}\cap U_i=T_i,
 \qquad
 U_i\cap Y_i=T_i.
\]

Thus (7.3) is one Johnson cycle through

\[
 3W+(W-c)=4W-c=W'
\]

distinct states, which is the whole child middle layer. \(\square\)

This theorem is an exact, integral central-owner recursion. It uses no
fractional selection and no unproved Hamilton completion. The next theorem
shows why it is not yet an optimal OR word.

## 8. Exact failure of the edge-local diamond chronology

### Theorem 8.1 (simultaneous residence/lower/upper failure)

In the Hamilton cycle (7.3):

1. every internal \(x\)-run is the two-state block \(A_iX_i\), and every
   internal \(y\)-run is \(Y_iA_i\);
2. there is no \(AA\) edge, so every both-new immediate-lower target
   \(R\cup\{x,y\}\), \(|R|=r-2\), is missing;
3. there is no \(UU\) edge, so every empty-signature immediate-upper
   target of rank \(r+2\) is missing.

Consequently, if the child deadline \(d'\ge2\), (7.3) is not resident and
cannot be the central row of an optimal flat word. Neither missing shadow
family can be created by a lower compiler.

#### Proof

The status pattern in each block is

\[
 [00],01,11,10.
\]

Only the last two states contain \(x\), and only the middle two contain
\(y\), giving the length-two runs. Exact depth-\(d'\) residence requires
every internal one-run to have length at least \(d'+1\).

An immediate-lower target containing both new coordinates can be the
intersection of two child middle states only if both states have status
\(11\), hence it needs an \(AA\) edge. An immediate-upper target avoiding
both new coordinates can be the union of two middle states only if both
have status \(00\), hence it needs a \(UU\) edge. Neither kind of edge
occurs in (7.3). Finally, Section 11 below proves that upper targets are
determined entirely by consecutive unions of the central chronology, so
lower pins cannot restore them. \(\square\)

This closes every edge-by-edge diamond substitution of the same status
pattern. A successful recursion must rebraid long \(A\)- and \(U\)-runs,
not merely change which occurrence of each \(V_i\) is selected.

## 9. The colored \(A\)-forest and exact residence hazards

For an old Hamilton path, complete its first-intersection sequence to a
rank-\((r-1)\) path

\[
 \widehat C=(C_0,\ldots,C_{W-1}).
\]

Color each of its \(W-1\) edges by the rank-\((r-2)\) intersection of its
endpoints. Assume every one of the \(W-c\) colors occurs.

An exact both-new first-lower forest must keep exactly one edge of each
color. It therefore keeps \(W-c\) edges, deletes \(c-1\), and has exactly
\(c\) path components.

Let \(D=d'+1\). Every internal old coordinate run of length
\(2\le\ell\le D\) induces a contiguous hazard interval of native
\(C\)-spine edges: if none of those edges is cut, the corresponding
\(A\)-component contains the trapped run

\[
 0\,1^{\ell-1}\,0
\]

of length less than \(D\).

### Theorem 9.1 (colored residence selector)

A chronological exact-color \(A\)-forest eliminates every internally
trapped short run if and only if one can choose one representative edge
from every color class so that no hazard interval is wholly selected.

Equivalently, every hazard interval must contain a deleted occurrence of a
repeated color.

#### Proof

An edge of a singleton color is forced to be kept. In a color class of
multiplicity \(m\), exact first-lower coverage keeps one occurrence and
deletes the other \(m-1\). By the definition of a hazard interval, a short
run survives exactly when every edge of its interval is kept. This gives
the equivalence. \(\square\)

Let \(R\) be the union of the nonsingleton color classes. Since

\[
 (W-1)-(W-c)=c-1
\]

is the total multiplicity excess,

\[
 \boxed{|R|\le2(c-1).}
\tag{9.1}
\]

Every deletable edge lies in \(R\). Hence a necessary condition is

\[
 \boxed{R\text{ meets every residence-hazard interval}.}
\tag{9.2}
\]

In particular, a hazard interval consisting only of globally unique colors
is a complete obstruction. This is strictly stronger than merely requiring
at most \(c-1\) edge-disjoint hazards.

Even after (9.2) passes, the exposed port runs must be fused. If the selected
\(A\)-forest components have sizes \(a_1,\ldots,a_c\), then positive
\(X\)-block lengths totaling \(W\) can make every new \(x\)-run at least
\(D\) exactly when

\[
 \boxed{\sum_{i=1}^{c}\max(1,D-a_i)\le W.}
\tag{9.3}

The same criterion holds independently for \(y\). Necessity is immediate;
sufficiency follows by assigning each component its minimum required block
and distributing the remaining positions arbitrarily. Old-coordinate port
runs remain a separate constraint.

## 10. The \(U\)-forest, upper providers, and rectangle rigidity

Return to a cyclic old carrier and put

\[
 V_i=T_i\cup T_{i+1}.
\]

Choose one occurrence index of each distinct \(V\)-color, and let \(I\)
be the selected set. Thus \(|I|=W-c\). Consecutive selected indices form
the natural \(U\)-path forest.

### Theorem 10.1 (exact \(U\)-sector first-lower gate)

For every selected run \([a,c]\), the two-port path

\[
 X_a-U_a-U_{a+1}-\cdots-U_c-Y_{c+1}
\tag{10.1}
\]

has first-lower colors

\[
 T_a,T_{a+1},\ldots,T_{c+1}.
\]

The union of these paths covers every neither-new immediate-lower color if
and only if

\[
 \boxed{\mathbb Z_W\setminus I\text{ is a stable set of the index cycle}.}
\tag{10.2}
\]

Equivalently, \(I\) must be a cycle vertex cover while containing exactly
one representative from each \(V\)-color class.

#### Proof

The port intersections are \(T_a\) and \(T_{c+1}\); each internal
\(U_iU_{i+1}\) intersection is \(T_{i+1}\). Thus (10.1) has precisely
the stated colors. A middle color \(T_j\) is uncovered exactly when both
adjacent indices \(j-1,j\) are omitted from \(I\), which is exactly an
adjacent pair in the complement. \(\square\)

The upper condition is stronger. For a deeper empty-signature upper target
\(Z\), let \(\mathcal O_Z\) be the family of old index intervals whose
consecutive \(V\)-union is \(Z\). Then inherited \(U\)-threading covers
\(Z\) exactly when

\[
 \boxed{\text{some }J\in\mathcal O_Z\text{ satisfies }J\subseteq I.}
\tag{10.3}
\]

If a provider interval repeats a \(V\)-color, it cannot be wholly retained
under the one-representative rule. Therefore, if every provider for one
\(Z\) repeats a color, that target is impossible in this architecture.

The local six-state rectangle does not reconcile the \(A\)- and \(U\)
selectors. For one old Johnson edge

\[
 T_i=C\cup\{u\},\qquad T_{i+1}=C\cup\{v\},
\]

suppress \(C\) and write

\[
 A=xy,\quad U=uv,\quad
 X_i=xu,\quad Y_i=yu,\quad
 X_{i+1}=xv,\quad Y_{i+1}=yv.
\]

The \(J(4,2)\) rectangle splits into the disjoint paths

\[
 Y_i-A-X_{i+1},
 \qquad
 X_i-U-Y_{i+1}.
\tag{10.4}
\]

Together they give the four first-lower colors

\[
 C\cup\{y\},\ C\cup\{x\},\ C\cup\{u\},\ C\cup\{v\}
\]

and the four first-upper colors obtained by adjoining \(C\) to the four
three-subsets of \(\{x,y,u,v\}\), each exactly once.

### Theorem 10.2 (global phase obstruction)

Suppose exactly one path in (10.4) is chosen at every old carrier edge and
every \(X_j,Y_j\) must be used exactly once. Then the choice is constant on
each connected old carrier cycle.

#### Proof

Let \(s_i=1\) for the \(U\)-path and \(s_i=0\) for the \(A\)-path. The
multiplicities of the cross states are

\[
 m(X_j)=s_j+(1-s_{j-1}),
 \qquad
 m(Y_j)=(1-s_j)+s_{j-1}.
\]

Both equal one if and only if \(s_j=s_{j-1}\). Connectivity forces a
constant phase. \(\square\)

Thus the locally first-shadow-perfect rectangle cannot implement arbitrary
colored \(A\)- and \(U\)-choices. Mixed phases require both/none defects,
open endpoints, or genuinely larger correlated packets. Moreover bounded
edgewise weaving retains the length-two new-coordinate runs of Theorem
8.1, so it does not solve residence or deeper upper shadows.

There is also an exact two-port restitution warning. Deleting a native
\(A_{i-1}A_i\) edge loses below

\[
 (C_{i-1}\cap C_i)\cup\{x,y\}
\]

and loses above \(T_i\cup\{x,y\}\). The seams

\[
 A_{i-1}-X_i,
 \qquad
 Y_i-A_i
\]

both restore the upper color, while their lower colors are
\(C_{i-1}\cup\{x\}\) and \(C_i\cup\{y\}\). The switch is therefore
first-shadow lossless only if the deleted both-new lower color has another
retained occurrence or is a permitted endpoint hole. Upper redundancy does
not imply lower restitution, and nothing in this switch controls deeper
collars.

## 11. Upper shadows are a central-carrier condition, not a lower Hall condition

### Theorem 11.1 (exact upper-union law)

If

\[
 D^dA=T,
\]

then every target \(Z\) of rank greater than \(r\) occurs in \(A\) if and
only if it is the union of a consecutive nonempty interval of central
states:

\[
 \boxed{
 Z=\bigcup_{h=i}^{j}T_h
 \quad\text{for some }0\le i\le j<W.}
\tag{11.1}
\]

#### Proof

An interval of \(A\) of length at most \(d+1\) lies inside a central
window and has rank at most \(r\). If an interval \([p,q]\) has length at
least \(d+2\), then

\[
 \bigcup_{a=p}^{q}A_a
 =\bigcup_{h=p}^{q-d}T_h.
\]

This proves necessity and sufficiency. \(\square\)

Thus a lower pin compiler can only shrink entries while preserving the
central equalities; it cannot create an absent upper provider. Every
candidate recursion must verify (11.1) for **all** upper ranks and all four
new-coordinate signatures.

For a piecewise braid, let \(I_q\) be the length-\((q+1)\) unions wholly
inside pieces and \(N_q\) those crossing new seams. Then exactly

\[
 \operatorname{supp}(D^qT)=I_q\cup N_q.
\tag{11.2}
\]

This is the correct collar ledger: removed cut-collar providers must be
replaced by new seam-collar providers at their actual ranks. First-shadow
counts do not imply (11.2) at \(q\ge2\).

There is already a nontrivial immediate-upper status cost. Let a child
middle permutation be split by \(x,y\)-status, let

\[
 n_-:=\binom{k}{r-1},
\]

and let \(c_{11}\) be the number of maximal both-new runs. Every target
\(S\cup\{x,y\}\), \(S\in\binom{[k]}r\), requires a distinct adjacent
central edge whose union is that target. At most \(n_--c_{11}\) such edges
are internal to both-new runs. Hence, if \(q\) is the number of eligible
cross-status transitions,

\[
 \boxed{q\ge W-n_-+c_{11}.}
\tag{11.3}
\]

For even \(k=2r\),

\[
 q\ge\frac{W}{r+1}+c_{11}\ge\frac{W}{r+1}+1.
\tag{11.4}
\]

Thus a bounded-piece pair-status lift fails already at upper depth one.
The exact \(12\to14\) construction evades this statement because it is a
one-coordinate six-piece braid, not a four-shore pair lift.

## 12. What the exact \(k=11,12,13,14\) words actually teach

The four exact words share the flat deadline form, exact residence, and all
upper shadows, but their carrier/compiler mechanisms are not recursive
copies of one SCD column.

* The \(k=11\) carrier is one lifted quotient cycle, depth-three resident,
  with complete lower and upper shadows. Its \(369\) slack units are all
  repeated lower occurrences.
* The \(k=12\) word comes from a six-piece odd-to-even braid at the lower
  deadline two. Its two units of depth loss are endpoint cells, and its
  remaining \(264\) slack units are repeated lower occurrences.
* The \(k=13\) carrier begins as two physical cycles and uses one
  shadow-safe cross-component splice. It has only two units of endpoint
  depth loss but \(1057\) repeated lower occurrences.
* The \(k=14\) carrier is a six-piece braid. Its new-coordinate run has the
  minimum legal length three, activating Corollary 4.2. It has one endpoint
  depth loss and \(391\) repeated lower occurrences.

The successful odd-to-even lifts \(11\to12\) and \(13\to14\) exploit a
deadline drop \(3\to2\): an intersection chronology loses one unit of run
length, which is acceptable at the smaller deadline. The same mechanism
does not supply a same-depth \(11\to13\) or \(13\to15\) sector. This is
why a formal four-sector copy of the finite words is not a \(k\mapsto k+2\)
proof.

Most importantly, (1.7) and (3.3) reconcile the small number of carrier
splices with the large lower migration. The splices organize the central
states; the lower compiler independently rematches hundreds or thousands
of repeated interior occurrences. Carrier seam count is not lower pin
migration count.

## 13. Exact conditional completion theorem

The preceding results identify the correct nonlocal successor rather than
another layerwise Hall problem.

### Theorem 13.1 (fail-closed same-parity completion)

Fix \(k\) and put \(d'=d(k+2)\). Suppose one constructs a permutation
\(T'\) of the child middle layer and an injective physical lower assignment
\(\phi'\) such that:

1. every internal coordinate one-run of \(T'\) has length at least
   \(d'+1\), including the exact port-gap conditions of Lemma 4.1 after
   the pins of \(\phi'\) are imposed;
2. the legal-position sets \(Q'_x\) defined by (4.3) satisfy (F1)--(F3);
3. every upper target of every new-coordinate signature is a consecutive
   union of \(T'\), equivalently (11.1), with every removed piece collar
   replaced as in (11.2).

Then the maximal word

\[
 A'_p=\{x:p\in Q'_x\}
\]

has length \(B(k+2)=W'+d'\), covers every nonempty child target, and hence

\[
 \nu(k+2)=B(k+2).
\]

#### Proof

(F1) gives every central equality; (F2) gives every assigned lower target;
(F3) makes every entry nonempty. Lemma 4.1 is the exact coordinatewise
residence test, so the central row is literally realized. Theorem 11.1
gives every upper target. The monotone-deadline lower bound supplies the
reverse inequality. \(\square\)

For a recursion built from the odd diamond deck, the following are proved
necessary subconditions on item 1--3:

* the colored \(A\)-selector of Theorem 9.1 and its port inequality (9.3);
* the stable-set and all-depth provider conditions (10.2)--(10.3) for
  \(U\);
* at least \(\Delta_0\) genuinely cross-status lower assignments;
* escape from the constant-phase invariant of Theorem 10.2;
* exact elimination of \(G\) source holes whenever the deadline does not
  jump;
* the complete upper collar ledger (11.2), not merely immediate shadow
  balance.

These conditions are not claimed sufficient by themselves; (F1)--(F3)
must still hold for one common labelled pin injection.

## 14. Precise proved/conditional boundary

### Proved

1. The endpoint-loss formula (1.5), with the corrected exact
   \(k=11,12,13,14\) profiles.
2. The all-\(k\), all-lower-rank integral containment matching of Theorem
   2.1.
3. The exact SCD overload (3.1), seam-local inequality (3.5), and positive
   asymptotic constant (3.7).
4. The minimum-residence physical counterexample and the exact
   residence-with-pins law.
5. The parity-unified deadline/slack recurrence (5.1)--(5.4).
6. The status-empty lower-capacity deficiency (6.3).
7. The explicit compressed-diamond Hamilton cycle through every child
   middle owner.
8. The simultaneous residence, lower-shadow, and upper-shadow failure of
   that edge-local chronology.
9. The colored \(A\)-hazard selector, stable/provider \(U\)-selector,
   \(J(4,2)\) constant-phase invariant, and exact upper-union law.

### Closed routes

The following implications are false or quantitatively impossible:

\[
 \text{containment Hall}\Rightarrow\text{literal lower compiler},
\]

\[
 \text{one SCD chain per owner plus bounded seams}
 \Rightarrow\text{optimal compiler},
\]

\[
 \text{first-shadow-perfect local rectangles}
 \Rightarrow\text{mixable global selectors},
\]

and

\[
 \text{central ownership plus lower Hall}
 \Rightarrow\text{residence and upper completeness}.
\]

### Open

The remaining lane-S gate is one growing, nonlocal correlated packet/braid
construction which simultaneously:

* reorders the full child middle deck into long resident status runs;
* makes the colored \(A\)- and provider \(U\)-choices without violating
  exact cross-state ownership;
* globally rematches the \(\Theta(W\sqrt{k})\) SCD-native lower overload;
* satisfies one common coordinatewise pin table (F1)--(F3); and
* restores every upper cut collar at every depth.

The exact \(k=11,\ldots,14\) words show that such global rebuilding is
possible at those four dimensions. They do not yet contain a
dimension-independent rule. This is the exact boundary of the present
SCD-seeded monotone-deadline route.
