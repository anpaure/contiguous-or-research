# Lane O: relative-to-absolute compiler installation and the Hall29 DM obstruction

**Date:** 2026-07-28  
**Lane:** O, owner-resolved installation translated to the finite
contiguous-OR compiler  
**Method:** pure mathematics. The numerical Hall29 block and its frozen
cut ledger are used only as audited finite input.

---

## 0. Outcome

Fix a middle chronology
\[
T=(T_0,\ldots,T_{W-1}),
\qquad
T_i\in\binom{[k]}r,
\qquad
W=\binom kr,
\]
and a delay \(d\). A proposed optimal word has length
\[
L=W+d
\]
and must satisfy
\[
D^dA=T.
\]

This report proves the following.

1. There is an exact relative-to-absolute installation theorem. Assign
   every lower target \(S\) injectively to a short compiler cell
   \(\phi(S)\). The assignment comes from one literal nonzero word if
   and only if the coordinatewise common allowed-position sets \(Q_x\)
   hit every positive central window, hit every positive assigned target
   interval, and cover every physical word position. When these
   conditions hold, the word is explicitly
   \[
   A_p=\{x:p\in Q_x\}.
   \]

2. Ordinary target--cell Hall is only the one-target projection of this
   theorem. It is necessary. A particular Hall matching certifies a word
   only after its simultaneous injection passes the common \(Q_x\) test;
   whether Hall zero always admits some such injection is not proved here.
   Overlapping target intervals can in principle destroy one another's
   coordinate witnesses.

3. At the projected allocation level, the exact unavoidable leave is
   the capacitated Hall deficiency
   \[
   \delta(G)
   =
   \max_{\mathcal A}
   \bigl(b(\mathcal A)-u(N_G(\mathcal A))\bigr)_+.
   \]
   With a frozen old installation, the same formula applied to residual
   demands and residual slot capacities is necessary and sufficient.

4. The relative-to-absolute transfer datum is therefore not one scalar
   owner-load \(L^1\) distance. It is the complete neighbourhood-rank
   profile
   \[
   r_G(\mathcal A)=u(N_G(\mathcal A)).
   \]
   For source and final graphs \(G_0,G_1\),
   \[
   \varepsilon_1(\mathcal A)
   =
   \varepsilon_0(\mathcal A)
   +r_{G_0}(\mathcal A)-r_{G_1}(\mathcal A),
   \qquad
   \varepsilon_i=b-r_{G_i}.
   \]
   Every lost unit of neighbourhood capacity must be paid from the old
   Hall surplus of the same target family.

5. If the relative source is already a matching in the exact cyclic
   compiler graph of a physical cyclic carrier, cutting and appending
   \(d\) prefix positions transfers that
   matching with **zero** lower Hall loss and adds
   \(\binom{d+1}{2}\) cells. If it is one common cyclic literal word,
   all lower targets transfer literally with zero loss. Thus “only
   \(d=3\) boundary loss” is not the correct dichotomy: a genuine source
   loses zero, while a bare owner/slot table has not yet supplied the
   required common matching or word.

6. Resident plus all-upper does **not** imply a lower installation with
   the optimal \(d=3\) boundary. The audited Hall29 carrier at \(k=15\)
   is an exact finite counterexample to that carrier-first implication.
   It is residence-perfect and has no
   upper holes, but its full lower compiler graph has
   \[
   16\,354/16\,383
   \]
   matching and deficiency \(29\).

7. Its frozen alternating-reachable Dulmage--Mendelsohn block is
   \[
   |\mathcal A_{29}|=1524,
   \qquad
   |N(\mathcal A_{29})|=1495.
   \]
   The graph used to compute this block already includes all three lower
   rows, all six triangular boundary-bonus cells, and the exact endpoint
   collars. (The six bonus cells are not themselves neighbours of this
   block.) Any repaired selected carrier must create at least \(29\)
   genuinely new, distinct neighbours of this same block before a perfect lower
   allocation is possible.

8. The sharp relative/gluing mismatch is visible on this block. Three
   separated upper-safe cuts expose isolated neighbourhood
   \[
   r_{\rm iso}(\mathcal A_{29})=1526,
   \]
   a surplus of \(2\). Re-gluing the four pieces into the resident
   Hamilton chronology reduces it to \(1495\), a loss of \(31\), and
   therefore
   \[
   -2+31=29.
   \]
   The failure is lost named-slot capacity under gluing, not target
   multiplicity.

Thus the proposed carrier-first implication is false. The exact
surviving gate is a joint construction of the resident/all-upper
chronology and a target-to-cell injection satisfying the common
\(Q_x\) conditions. Hall zero is necessary; after Hall zero, the joint
coordinate conditions still have to be checked.

---

## 1. The finite lower compiler

For a set word
\[
A=(A_0,\ldots,A_{L-1})
\]
put
\[
(D^qA)_a=\bigcup_{p=a}^{a+q}A_p.
\tag{1.1}
\]

Let
\[
T=(T_0,\ldots,T_{W-1})
\]
be a permutation of the middle layer \(\binom{[k]}r\). We seek
\[
D^dA=T.
\tag{1.2}
\]

The central window belonging to \(T_i\) is
\[
J_i=[i,i+d].
\tag{1.3}
\]
The short lower compiler cells are
\[
\mathcal C_d
=
\{(q,a):0\le q<d,\ 0\le a<L-q\}.
\tag{1.4}
\]
We identify \(c=(q,a)\) with its physical interval
\[
I(c)=[a,a+q].
\tag{1.5}
\]

Their exact number is
\[
|\mathcal C_d|
=
\sum_{q=0}^{d-1}(W+d-q)
=dW+\binom{d+1}{2}.
\tag{1.6}
\]

Let
\[
\mathcal L_{<r}
=
\{S\subseteq[k]:1\le |S|<r\}
\tag{1.7}
\]
be the lower target family.

### Lemma 1.1 (every lower target lies in the short band)

If \(D^dA=T\) and \(|S|<r\), then an interval whose union is \(S\)
has length at most \(d\). Equivalently, every lower target occurs in
one of the cells (1.4).

#### Proof

Every interval of length at least \(d+1\) contains a subinterval
\([i,i+d]\). Its union contains
\[
\bigcup_{p=i}^{i+d}A_p=T_i,
\]
which has rank \(r\). The whole interval union therefore has rank at
least \(r\). ∎

### Lemma 1.2 (upper transfer)

If \(D^dA=T\), then for every \(q\) for which both sides are defined
(equivalently, \(0\le q\le W-1\)),
\[
D^{d+q}A=D^qT.
\tag{1.8}
\]

#### Proof

At start \(i\), both sides of (1.8) are the union of
\[
A_i,A_{i+1},\ldots,A_{i+d+q}.
\]
∎

Consequently a resident chronology whose consecutive unions contain
every upper target leaves only the finite lower installation problem.

---

## 2. Exact joint target installation

Choose an injection
\[
\phi:\mathcal L_{<r}\longrightarrow\mathcal C_d.
\tag{2.1}
\]
Thus \(\phi(S)\) is the short cell in which target \(S\) is to occur.
Injection is necessary because one cell has only one value.

For every coordinate \(x\in[k]\), define its maximal common allowed
position set
\[
Q_x(\phi)
=
[0,L-1]\setminus
\left(
\bigcup_{\substack{0\le i<W\\x\notin T_i}}J_i
\ \cup\
\bigcup_{\substack{S\in\mathcal L_{<r}\\x\notin S}}I(\phi(S))
\right).
\tag{2.2}
\]

The first union encodes all negative central requirements. The second
encodes all negative assigned-target requirements.

### Theorem 2.1 (exact relative-to-absolute compiler installation)

For the fixed chronology \(T\) and injection \(\phi\), there exists a
nonzero word \(A=(A_p)_{p=0}^{L-1}\) such that
\[
D^dA=T
\tag{2.3}
\]
and
\[
\bigcup_{p\in I(\phi(S))}A_p=S
\qquad(S\in\mathcal L_{<r})
\tag{2.4}
\]
if and only if all three conditions below hold:

1. **central positive hitting**
   \[
   J_i\cap Q_x(\phi)\ne\varnothing
   \qquad(0\le i<W,\ x\in T_i);
   \tag{2.5}
   \]

2. **target positive hitting**
   \[
   I(\phi(S))\cap Q_x(\phi)\ne\varnothing
   \qquad(S\in\mathcal L_{<r},\ x\in S);
   \tag{2.6}
   \]

3. **nonzero physical entries**
   \[
   \bigcup_{x\in[k]}Q_x(\phi)=[0,L-1].
   \tag{2.7}
   \]

When these conditions hold, an explicit realizing word is
\[
\boxed{
A_p=\{x:p\in Q_x(\phi)\}.}
\tag{2.8}
\]

#### Proof

Suppose first that \(A\) realizes (2.3)--(2.4). If \(x\notin T_i\),
then \(x\) is absent throughout \(J_i\); if \(x\notin S\), then it is
absent throughout \(I(\phi(S))\). Hence the support of coordinate
\(x\) in \(A\) is contained in \(Q_x(\phi)\).

If \(x\in T_i\), equality (2.3) forces some occurrence of \(x\) in
\(J_i\), proving (2.5). If \(x\in S\), equality (2.4) forces some
occurrence in \(I(\phi(S))\), proving (2.6). Since every \(A_p\) is
nonempty, some coordinate support contains \(p\), proving (2.7).

Conversely, define \(A\) by (2.8). If \(x\notin T_i\), definition
(2.2) excludes \(x\) from every \(A_p\), \(p\in J_i\). If
\(x\in T_i\), condition (2.5) includes it at least once. Therefore
\[
\bigcup_{p\in J_i}A_p=T_i.
\]
The identical argument using the second union in (2.2) and condition
(2.6) proves (2.4). Condition (2.7) makes every \(A_p\) nonempty. ∎

### Corollary 2.2 (relative extension with frozen resident targets)

Let \(\phi_0\) be a prescribed injective assignment on a subfamily
\(\mathcal R\subseteq\mathcal L_{<r}\). It extends, without moving any
pair in \(\phi_0\), to one literal word installing all lower targets if
and only if there is an injection
\[
\psi:
\mathcal L_{<r}\setminus\mathcal R
\longrightarrow
\mathcal C_d\setminus\phi_0(\mathcal R)
\]
such that the combined injection
\[
\phi=\phi_0\cup\psi
\]
satisfies (2.5)--(2.7).

If the old resident assignments may move, the same theorem applies with
\(\phi\) chosen freely on the whole lower family.

This is the literal relative-to-absolute theorem. It exposes a feature
absent from the earlier owner-load calculation: inserting a new target
pin removes coordinate positions from \(Q_x\), and can therefore destroy
old central or target witnesses even when its compiler cell was unused.

### Corollary 2.3 (completion to a universal word)

Assume \(T\) contains every upper target in its consecutive-union rows.
Then an injection satisfying Theorem 2.1 produces a universal nonzero
contiguous-OR word of length \(W+d\).

#### Proof

Theorem 2.1 gives all lower targets and the middle permutation. Lemma
1.2 transfers the upper coverage of \(T\) to \(A\). ∎

---

## 3. The Hall projection

For a target \(S\) and cell \(c\), call \(S\sim c\) if \(c\) passes the
one-target compiler compatibility test for the fixed carrier. Equivalently,
the assignment \(\phi(S)=c\), with no other lower target pinned, passes
the corresponding single-target version of (2.5)--(2.7). Let
\[
G_T\subseteq\mathcal L_{<r}\times\mathcal C_d
\tag{3.1}
\]
be this target--cell graph. The audited flexible compiler graph may
also be used here; the only property needed below is that every actual
target occurrence gives an edge.

### Proposition 3.1 (Hall is necessary; the joint test remains)

Every literal installation from Theorem 2.1 induces a matching in
\(G_T\) saturating \(\mathcal L_{<r}\).

The converse does not follow from the matching certificate alone. A matching
checks every target separately, whereas (2.2) intersects all negative target
requirements on every shared physical position. A particular matching is
absolute only when its injection also satisfies the joint conditions
(2.5)--(2.7). It remains possible that some other perfect matching passes;
no Hall-zero/nonliteral counterexample is asserted here.

#### Proof

The realizing injection is already one-to-one. Restricting a feasible
joint pin system to one target preserves feasibility, so every selected
pair is an edge of \(G_T\). The second assertion is exactly the
difference between the one-target and simultaneous definitions of
\(Q_x\). ∎

Thus a Hall failure is terminal, while a Hall pass is followed by the
common-core/pin test.

---

## 4. Capacitated relative Hall installation

The preceding graph is unit-capacitated in the finite compiler, but the
right general translation of owner loads uses demands and capacities.

Let \(\mathcal T\) be target types with integer demands \(b_t\), let
\(\mathcal S\) be slots with integer capacities \(u_s\), and let
\[
G\subseteq\mathcal T\times\mathcal S
\]
be the allowed incidence graph. For
\(\mathcal A\subseteq\mathcal T\), put
\[
b(\mathcal A)=\sum_{t\in\mathcal A}b_t,
\qquad
r_G(\mathcal A)
=
\sum_{s\in N_G(\mathcal A)}u_s.
\tag{4.1}
\]

### Theorem 4.1 (exact capacitated Hall leave)

The minimum number of uninstalled target units is
\[
\boxed{
\delta(G;b,u)
=
\max_{\mathcal A\subseteq\mathcal T}
\bigl(b(\mathcal A)-r_G(\mathcal A)\bigr)_+.}
\tag{4.2}
\]
In particular, every target unit installs integrally if and only if
\[
r_G(\mathcal A)\ge b(\mathcal A)
\qquad(\mathcal A\subseteq\mathcal T).
\tag{4.3}
\]

#### Proof

Use the integral network
\[
\text{source}\longrightarrow\mathcal T
\longrightarrow\mathcal S
\longrightarrow\text{sink}
\]
with capacities \(b_t\), infinity on allowed target--slot arcs, and
\(u_s\), respectively. Every finite cut is determined by a target
family \(\mathcal A\) and has capacity at least
\[
b(\mathcal T\setminus\mathcal A)+r_G(\mathcal A)
=
b(\mathcal T)
-
\bigl(b(\mathcal A)-r_G(\mathcal A)\bigr).
\]
Taking \(N_G(\mathcal A)\) on the source side attains this value.
Max-flow/min-cut gives (4.2), and integral capacities give an integral
allocation. ∎

### Theorem 4.2 (frozen relative installation)

Let \(F\) be an old target--slot assignment which must remain fixed.
Subtract its fulfilled demand and occupied capacity:
\[
b_t^F=b_t-\deg_F(t),
\qquad
u_s^F=u_s-\deg_F(s).
\tag{4.4}
\]
Then the exact additional leave is
\[
\boxed{
\delta_F
=
\max_{\mathcal A\subseteq\mathcal T}
\left(
b^F(\mathcal A)
-
\sum_{s\in N_G(\mathcal A)}u_s^F
\right)_+.}
\tag{4.5}
\]
Hence \(F\) extends to an absolute allocation if and only if every
residual Hall inequality is nonnegative.

#### Proof

Delete the demand and capacity already consumed by \(F\), and apply
Theorem 4.1 to the residual network. ∎

In the unit-demand, unit-capacity compiler, if old pairs may be released,
assume an absolute allocation exists and let \(F_0\) be the old matching.
The minimum number of old pairs which must move is
\[
|F_0|
-
\max\{
|M\cap F_0|:
M\text{ is an absolute saturating allocation}
\}.
\tag{4.6}
\]
The maximum is an integral maximum-weight matching, with weight one on
old pairs and zero elsewhere. This is the exact target--slot analogue
of minimum-disturbance owner installation.

All statements in this section are for one **fixed** incidence graph.
Adding literal target pins can shrink the common sets \(Q_x\) and thereby
change compatibility itself; that nonlinear update is not absorbed by the
residual capacities in (4.4). After any such update, the graph and all Hall
cuts must be recomputed, or Theorem 2.1 must be applied directly.

---

## 5. Relative-to-absolute Hall profiles

For source and final graphs \(G_0,G_1\) with the same target demands,
define
\[
\varepsilon_i(\mathcal A)
=
b(\mathcal A)-r_{G_i}(\mathcal A).
\tag{5.1}
\]

### Theorem 5.1 (exact cut-profile transfer identity)

For every target family \(\mathcal A\),
\[
\boxed{
\varepsilon_1(\mathcal A)
=
\varepsilon_0(\mathcal A)
+
r_{G_0}(\mathcal A)-r_{G_1}(\mathcal A).}
\tag{5.2}
\]
If \(G_0\) is installable, then \(G_1\) is installable at the projected
Hall level if and only if
\[
r_{G_0}(\mathcal A)-r_{G_1}(\mathcal A)
\le
r_{G_0}(\mathcal A)-b(\mathcal A)
\qquad(\mathcal A\subseteq\mathcal T).
\tag{5.3}
\]

#### Proof

Equation (5.2) is subtraction of the definitions. By Theorem 4.1,
\(G_1\) is installable exactly when
\(\varepsilon_1(\mathcal A)\le0\) for every \(\mathcal A\).
Substitute (5.2) and rearrange. ∎

Equivalently, without assuming that the source graph is installable,
\[
\boxed{
\delta(G_1;b,u)
=
\max_{\mathcal A\subseteq\mathcal T}
\left(
\varepsilon_0(\mathcal A)
+r_{G_0}(\mathcal A)-r_{G_1}(\mathcal A)
\right)_+.}
\tag{5.4}
\]
In the unit case, if
\[
v_{01}(\mathcal A)
=|N_{G_1}(\mathcal A)|-|N_{G_0}(\mathcal A)|,
\]
then absolute projected Hall is exactly the full family
\[
v_{01}(\mathcal A)
\ge
|\mathcal A|-|N_{G_0}(\mathcal A)|
\qquad(\mathcal A\subseteq\mathcal T).
\tag{5.5}
\]

The left side of (5.3) is the neighbourhood capacity lost in passing
from the relative source to the final contiguous compiler. The right
side is the old surplus on the same target family.

This is the precise translation of the earlier owner-resolved theorem.
In the owner-load setting, there was no target-dependent incidence
restriction after a slot was freed, so an aggregate occurrence-vector
distance controlled the answer. In the compiler, different targets
see different slots. The complete submodular profile
\[
\mathcal A\longmapsto r_G(\mathcal A)
\]
is indispensable. Total slot count is only the single cut
\(\mathcal A=\mathcal T\), and pointwise source supply checks only
singleton cuts.

### Theorem 5.2 (cyclic-to-linear transfer does not increase Hall deficiency)

Let \(T=(T_0,\ldots,T_{W-1})\) be a physical cyclic depth-\(d\)
carrier, where \(1\le d<W\). Define its cyclic maximal erosion by
\[
P_j^\circ
=
\bigcap_{h=0}^{d}T_{j-h\pmod W}.
\tag{5.6}
\]
The physical hypothesis means \(D_\circ^dP^\circ=T\); in particular,
every required middle
coordinate has a nonempty cyclic carrier set.
Cut at \(0\), unroll the word to positions \(0,\ldots,W+d-1\), and put
\[
P_p^\ell
=
\bigcap_{\max(0,p-d)\le t\le\min(p,W-1)}T_t.
\tag{5.7}
\]
Let \(G_T^\circ\) and \(G_T^\ell\) be the exact one-target
maximal-erosion candidate graphs for the cyclic and linear carriers,
respectively. Then mapping a cyclic lower cell \((q,s)\), where
\[
0\le q<d,
\qquad
0\le s<W,
\]
to the linear cell on the same unrolled interval \([s,s+q]\) gives an
injective edge-preserving map
\[
G_T^\circ\hookrightarrow G_T^\ell.
\tag{5.8}
\]
Consequently
\[
\boxed{
\delta(G_T^\ell)\le\delta(G_T^\circ).}
\tag{5.9}
\]
Every cyclic Hall matching transfers unchanged. Linearization also adds
exactly
\[
\sum_{q=0}^{d-1}(d-q)=\binom{d+1}{2}
\tag{5.10}
\]
lower cells. At \(d=3\), the projected lower Hall loss is zero and the
linear graph has six additional cells; it is not a three-slot-loss
problem.

#### Proof

For every unrolled position \(p\), linearization removes only the cyclic
middle-window constraints which cross the cut. Hence
\[
P_{p\bmod W}^\circ\subseteq P_p^\ell.
\tag{5.11}
\]
For \(x\in T_t\), first define its cyclic carrier set in
\(\mathbb Z/W\mathbb Z\), and then its representatives in the unrolled
top interval, by
\[
\begin{aligned}
K_{\rm cyc}^\circ(t,x)
&=\{j\in[t,t+d]_{\rm cyc}:x\in P_j^\circ\},\\
\widetilde K^\circ(t,x)
&=\{p\in[t,t+d]:p\bmod W\in K_{\rm cyc}^\circ(t,x)\},\\
K^\ell(t,x)
&=\{p\in[t,t+d]:x\in P_p^\ell\}.
\end{aligned}
\tag{5.12}
\]
Equation (5.11) gives
\[
\widetilde K^\circ(t,x)\subseteq K^\ell(t,x).
\tag{5.13}
\]
The cyclic factorability hypothesis makes every
\(K_{\rm cyc}^\circ(t,x)\) nonempty.

For an unrolled cell interval \(C=[s,s+q]\), let
\[
C^\circ=\{p\bmod W:p\in C\}.
\]
The cyclic envelope and mandatory mask are
\[
E_{C^\circ}^\circ=\bigcup_{j\in C^\circ}P_j^\circ,
\qquad
M_{C^\circ}^\circ
=
\{x:\text{for some }t,\ x\in T_t,\ 
       \varnothing\ne K_{\rm cyc}^\circ(t,x)\subseteq C^\circ\}.
\tag{5.14}
\]
Define \(E_C^\ell,M_C^\ell\) by the same formulas with
\(P^\ell,K^\ell,C\). The exact one-target fit predicate in either model
is
\[
M_C\subseteq S\subseteq E_C,
\qquad
S\cap P_p\ne\varnothing\quad(p\in C).
\tag{5.15}
\]
Under the cell map, (5.11)--(5.13) imply
\[
E_{C^\circ}^\circ\subseteq E_C^\ell,
\qquad
M_C^\ell\subseteq M_{C^\circ}^\circ,
\tag{5.16}
\]
because \(K^\ell(t,x)\subseteq C\) implies
\(\widetilde K^\circ(t,x)\subseteq C\), hence
\(K_{\rm cyc}^\circ(t,x)\subseteq C^\circ\). Every positionwise
nonempty test only becomes easier. Therefore a
target fitting a cyclic cell fits its linear image. The cell map is
injective because distinct cyclic starts \(0,\ldots,W-1\) remain distinct
unrolled starts. It preserves every matching, proving (5.9).

There are \(W\) cyclic cells in each of the \(d\) short rows. Equation
(1.6) gives the linear count; their difference is (5.10). ∎

### Corollary 5.3 (literal cyclic lower installation also has zero loss)

Suppose a cyclic nonzero word
\[
A^\circ=(A_0,\ldots,A_{W-1})
\]
has cyclic depth-\(d\) row \(T\) and already realizes every lower target
in a cyclic short cell. Then
\[
A=(A_0,\ldots,A_{W-1},A_0,\ldots,A_{d-1})
\tag{5.17}
\]
is a linear word of length \(W+d\) with middle row \(T\) and the same
lower coverage. Every noncrossing upper occurrence transfers. No coverage
claim is automatic for an upper target whose only known cyclic occurrences
cross the chosen cut.

#### Proof

Every cyclic interval of length at most \(d\) occurs literally in the
unrolled word, using the appended prefix when necessary. The same is true
for all \(W\) cyclic intervals of length \(d+1\), so its depth-\(d\) row
is exactly the linearized \(T\). Longer upper intervals are governed by
Lemma 1.2 and may lose a crossing-cut carrier occurrence. ∎

Theorem 5.2 identifies the precise interface mismatch. If the
owner-resolved source theorem supplied a physical cyclic candidate matching,
the projected lower allocation would transfer with zero loss. If it supplied
one common cyclic literal word, Corollary 5.3 would transfer all lower
targets literally. Merely renaming lower targets as owners and compiler cells
as slots supplies neither object: it forgets target-dependent Hall cuts and,
at the literal level, the shared word variables. The Hall29 graph below shows
that a selected resident/all-upper carrier can fail even the necessary
linear matching gate.

---

## 6. A selected DM block and its repair law

We now specialize to unit target demands and unit slot capacities.

### Theorem 6.1 (selected alternating-reachable deficient DM union)

Let \(M\) be a maximum matching in \(G=(\mathcal T,\mathcal S)\), and
let \(U\subseteq\mathcal T\) be its unmatched targets. From \(U\),
follow alternating paths, beginning with unmatched target--slot edges.
Let \(\mathcal A_{\rm DM}\) and \(\mathcal B_{\rm DM}\) be the reachable
target and slot shores.

Then
\[
\mathcal B_{\rm DM}=N_G(\mathcal A_{\rm DM})
\tag{6.1}
\]
and
\[
\boxed{
|\mathcal A_{\rm DM}|-|\mathcal B_{\rm DM}|
=|U|
=|\mathcal T|-|M|
=\delta(G).}
\tag{6.2}
\]

#### Proof

If a reachable target had a neighbour outside
\(\mathcal B_{\rm DM}\), the corresponding unmatched-direction edge
would make that slot reachable, proving (6.1). No reachable slot is
unmatched, or there would be an augmenting path from \(U\).

Every reachable slot is therefore matched to a reachable target.
Conversely, every reachable target outside \(U\) was reached through
its matching edge. The matching edges consequently give a bijection
\[
\mathcal B_{\rm DM}
\longleftrightarrow
\mathcal A_{\rm DM}\setminus U.
\]
This proves (6.2). The last equality is Theorem 4.1 in the unit case.
∎

The alternating-reachable union is a selected witness relative to the
chosen maximum matching; uniqueness among all maximum-deficiency shores
is not asserted: balanced DM components may be adjoined without changing
the deficiency.

### Corollary 6.2 (selected-DM slot-creation law)

Let \(G'\) be any repaired target--slot graph on the same targets,
possibly with additional slots. If \(G'\) has a matching saturating
all targets, then
\[
|N_{G'}(\mathcal A_{\rm DM})|
\ge
|N_G(\mathcal A_{\rm DM})|+\delta(G).
\tag{6.3}
\]
Equivalently,
\[
\boxed{
|N_{G'}(\mathcal A_{\rm DM})
\setminus N_G(\mathcal A_{\rm DM})|
\ge\delta(G).}
\tag{6.4}
\]

Thus a repair which can make at most \(b\) distinct slots newly adjacent
to the selected block cannot succeed when \(b<\delta(G)\).

#### Proof

Hall in \(G'\) gives
\[
|N_{G'}(\mathcal A_{\rm DM})|
\ge|\mathcal A_{\rm DM}|
=|N_G(\mathcal A_{\rm DM})|+\delta(G).
\]
If old neighbours are lost, still more new neighbours are required,
so (6.4) follows. ∎

Paying one selected block is necessary, not sufficient after the graph
changes. A different deficient DM block may appear. The exact
criterion remains the complete family (4.3), or equivalently repeated
DM separation until the deficiency is zero.

---

## 7. The \(k=15,d=3\) specialization

Put
\[
k=15,
\qquad
r=8,
\qquad
W=\binom{15}{8}=6435,
\qquad
d=3.
\tag{7.1}
\]
The optimal target length would be
\[
L=W+d=6438.
\tag{7.2}
\]

The lower target family has size
\[
|\mathcal L_{<8}|
=
\sum_{j=1}^{7}\binom{15}{j}
=16383.
\tag{7.3}
\]
The three lower compiler rows have lengths
\[
W+3,\qquad W+2,\qquad W+1,
\]
and hence
\[
|\mathcal C_3|
=3W+6
=19311.
\tag{7.4}
\]
The scalar surplus is
\[
19311-16383=2928.
\tag{7.5}
\]

The three appended physical positions create the triangular bonus
\[
\binom{d+1}{2}=6
\tag{7.6}
\]
compiler cells beyond the \(3W\) cyclic/interior count. They do not
create merely three abstract universal Hall slots. The 36 endpoint objects
used by the exact Benders evaluator are boundary-affected physical compiler
cells already counted among the \(19311\) cells, not 36 additional cells
and not a matching-loss bound. Theorem 5.2 gives zero projected Hall loss
when a genuine cyclic source matching exists.

---

## 8. Hall29 is an exact carrier-first counterexample

Let \(P_{29}\) be the audited carrier
scratch/k15_doubletrans_05_213_hall29.json. The finite input used here
is:

- it is one Hamilton path through all \(6435\) middle masks;
- it has zero depth-three residence defects;
- it has zero upper holes at every depth \(1,\ldots,7\);
- its full flexible lower graph contains all \(19311\) linear cells and
  exact boundary/collar candidates; this is precisely the exact
  maximal-erosion graph \(G^\ell\) of (5.14)--(5.15);
- its maximum matching has size
  \[
  16354,
  \]
  and hence deficiency \(29\).

The frozen alternating-reachable DM block satisfies
\[
\boxed{
|\mathcal A_{29}|=1524,
\qquad
|N_{P_{29}}(\mathcal A_{29})|=1495.}
\tag{8.1}
\]
Its target-rank histogram is
\[
\begin{array}{c|rrrr}
\text{rank}&4&5&6&7\\ \hline
\#\text{ targets}&9&82&412&1021,
\end{array}
\tag{8.2}
\]
and its neighbour-depth histogram is
\[
\begin{array}{c|rrr}
\text{cell depth}&0&1&2\\ \hline
\#\text{ cells}&81&395&1019.
\end{array}
\tag{8.3}
\]
Both rows sum to \(1524\) and \(1495\), respectively.

### Theorem 8.1 (no optimal word through the Hall29 carrier)

There is no nonzero word of length \(6438\) satisfying
\[
D^3A=P_{29}
\]
and covering every lower target. In particular, residence plus complete
upper coverage does not imply an optimal lower installation.

#### Proof

Every such word would induce, by Lemma 1.1 and Proposition 3.1, a
matching saturating all \(16383\) lower targets in the audited full
compiler graph. But (8.1) violates Hall by \(29\). ∎

This conclusion uses only the necessary projected graph. It does not
assume that a Hall pass would be sufficient for the joint literal
compiler.

Moreover, if this ordered carrier arose by cutting a physical cyclic
carrier, Theorem 5.2 would give
\[
\delta(G^\circ)\ge\delta(G^\ell)=29.
\tag{8.4}
\]
Thus a cyclic relative Hall source on the same carrier would already be
impossible. Under this conditional hypothesis, the deficiency cannot be
charged to cutting or to the three appended positions. No cyclic closure
of the Hall29 endpoints is asserted.

Seven Hall29 targets have degree zero, but that is not the whole
obstruction. The DM block contains \(1524\) targets and loses \(29\)
units through shared neighbours. Supplying an individual motif for
each of the seven zeros therefore does not prove a simultaneous
installation.

The scalar surplus \(2928\) in (7.5) also does not help: almost all of it
lies outside \(N(\mathcal A_{29})\). Corollary 6.2 says that any repaired
selected carrier must create at least \(29\) distinct new neighbours of
\(\mathcal A_{29}\). The full graph behind (8.1) already contains all six
boundary-bonus cells and every endpoint-affected physical cell; none of the
six bonus cells is adjacent to \(\mathcal A_{29}\). In the standard
row-flattening their indices are
\[
6435,\ 6436,\ 6437,\ 12873,\ 12874,\ 19310,
\tag{8.5}
\]
and none occurs in the frozen DM neighbour list. There is no unpriced
\(d=3\) boundary reserve.

Even granting, counterfactually, three new universal block-neighbours and
losing none of the old ones would leave
\[
1524-(1495+3)=26
\tag{8.6}
\]
unmatched units on this same Hall cut. A genuine repair must satisfy the
net gain condition
\[
\#\{\text{new block-neighbours}\}
-
\#\{\text{old block-neighbours lost}\}
\ge29.
\tag{8.7}
\]

---

## 9. The boundary has capacity two at the first lower shadow

There is a simpler hand obstruction which agrees with the DM block.

### Lemma 9.1 (two rank-\((r-1)\) boundary channels)

Let \(T\) be a Johnson path and let \(D^dA=T\). A rank-\((r-1)\)
short cell which does not lie on either of the two boundary chains equals
\[
T_i\cap T_{i+1}
\]
for some path edge \(i\).

The cells exceptional to this statement lie on one left and one right
boundary chain. Each chain is nested and can contain at most one
distinct rank-\((r-1)\) target. Hence the two boundaries together can
repair at most two missing first-shadow colours, independently of \(d\).

#### Proof

Let \(C=(D^qA)_a\), \(q<d\), have rank \(r-1\). The central windows
containing its physical interval \([a,a+q]\) have starts
\[
a+q-d\le i\le a,
\tag{9.1}
\]
after truncation to \(0\le i<W\). Away from the two extreme boundary
chains, this interval contains two consecutive starts \(i,i+1\).
Therefore
\[
C\subseteq T_i\cap T_{i+1}.
\]
Johnson adjacency gives
\[
|T_i\cap T_{i+1}|=r-1,
\]
so equality holds.

At either end, the exceptional short cells form a chain of nested
physical intervals, and their unions are nested. Two distinct nested
sets cannot both have rank \(r-1\). ∎

### Corollary 9.2 (the Hall29 first-shadow failure)

The Hall29 path has four missing rank-seven edge colours. At most two
can be supplied by the two boundary chains. Thus at least two remain
missing in every depth-three factor word.

In particular, the phrase “\(d=3\) boundary loss” must not be read as
three independent first-shadow repairs. The exact first-shadow boundary
capacity is two.

The DM obstruction is stronger: it couples ranks \(4,5,6,7\) and forces
leave \(29\), not merely the two first-shadow failures.

---

## 10. The exact isolated-to-glued mismatch

For a fixed target family \(\mathcal A\), write
\[
h_{\mathcal A}(P)=|N_P(\mathcal A)|
\tag{10.1}
\]
for its compiler neighbourhood under a factorable carrier piece or
chronology.

### Proposition 10.1 (neighbourhood subadditivity under gluing)

If \(P,Q\), and their concatenation \(PQ\), are factorable, then
\[
h_{\mathcal A}(PQ)
\le
h_{\mathcal A}(P)+h_{\mathcal A}(Q).
\tag{10.2}
\]

#### Proof

Map a compiler cell of \(PQ\), according to its start, to the
corresponding cell of isolated \(P\) or isolated \(Q\). The two image
families are disjoint. Gluing introduces additional central-window
constraints near the seam. Thus the maximal erosion envelope can only
shrink, admissible carrier sets can only shrink, and mandatory coordinate
sets can only grow. Any target accepted by the glued cell was therefore
accepted by its isolated image. The cell map is injective, proving
(10.2). ∎

The audited Hall29 cut ledger gives three separated upper-safe cuts with
individual gains
\[
10,\qquad11,\qquad10.
\tag{10.3}
\]
For the resulting four isolated pieces,
\[
h_{\mathcal A_{29}}(\text{isolated pieces})=1526.
\tag{10.4}
\]
Since \(|\mathcal A_{29}|=1524\), this relative source has Hall surplus
\[
1526-1524=2
\tag{10.5}
\]
on the selected block.

Re-gluing the pieces in their original Hall29 order returns to
\[
h_{\mathcal A_{29}}(P_{29})=1495.
\tag{10.6}
\]
Thus gluing destroys
\[
1526-1495=31
\tag{10.7}
\]
named block-compatible slots. The transfer identity (5.2) becomes
\[
\underbrace{1524-1526}_{-2}
+
\underbrace{1526-1495}_{31}
=
\underbrace{1524-1495}_{29}.
\tag{10.8}
\]

This is the requested exact relative-to-absolute mismatch. The isolated
four-piece system is a disconnected Hall relaxation, not an absolute word.
It clears the chosen Hall cut, but the contiguous chronology
spends \(31\) units of its neighbourhood capacity while only \(2\) units
of surplus were available.

No theorem based only on target multiplicities, point support, or total
slot count can see (10.8). The complete cut profile is necessary.

---

## 11. Relation to the relabel-parent source theorem

The coordinate-relabel parent theorem proves that one relabelled Hall29
parent can supply parent-pure motifs for all seven old zero-candidate
targets. This is a genuine source theorem. It closes point support in
the two-parent catalogue.

It does not contradict Theorem 8.1:

1. catalogue motifs compete for successor arcs and physical cells;
2. a selected carrier retains only one admissible chronology;
3. full point support checks singleton Hall cuts only;
4. \(\mathcal A_{29}\) is a \(1524\)-target cut with deficiency \(29\);
5. mixed-parent seams can shrink the joint neighbourhood and can violate
   the common \(Q_x\) conditions.

Indeed, the exact two-parent cube can escape the first selected block,
but the full-boundary audit exposes another
\[
1524-1495=29
\]
block. Imposing both exact inequalities makes that cube infeasible.
This finite fact illustrates the general warning after Corollary 6.2:
paying one DM block need not make the absolute Hall profile nonnegative.

---

## 12. Proved and open boundary

### Proved

1. The exact joint \(Q_x\) criterion, Theorem 2.1, for installing all
   lower targets into one literal factor word.
2. The exact frozen-assignment relative extension criterion.
3. The capacitated Hall leave formula and its residual/frozen version.
4. The minimum-disturbance maximum-weight matching formulation.
5. The exact Hall cut-profile transfer identity.
6. The zero-loss cyclic-to-linear Hall embedding and the zero-loss literal
   prefix append theorem.
7. The selected DM block formula and the \(29\)-new-slot repair law.
8. The exact lower-cell count
   \[
   dW+\binom{d+1}{2},
   \]
   equal to \(19311\) at \(k=15,d=3\).
9. The two-channel first-shadow boundary theorem.
10. The Hall29 carrier-first obstruction.
11. The isolated surplus \(2\), gluing loss \(31\), final deficiency
    \(29\) ledger.

### Not proved

1. A resident, all-upper \(k=15\) carrier whose full lower Hall
   deficiency is zero.
2. That projected Hall zero alone implies the joint \(Q_x\) conditions.
3. A motif-preserving successor-factor selection from the relabel-parent
   catalogue with nonnegative Hall profile on every target family.
4. A theorem preventing a new DM block from appearing after the
   selected Hall29 block is repaired.
5. A length-\(6438\) universal word at \(k=15\).

### Exact surviving target

Construct simultaneously:

1. a middle permutation \(T\) with depth-three residence;
2. complete upper coverage;
3. an injection
   \[
   \phi:\mathcal L_{<8}\to\mathcal C_3
   \]
   satisfying all Hall inequalities; and
4. the common coordinate conditions (2.5)--(2.7).

Then Theorem 2.1 and Lemma 1.2 give a literal word of length
\[
W+3=6438.
\]

The proved strict implication failure is
\[
\text{resident/all-upper carrier}
\not\Rightarrow
\text{Hall zero}
\]
by Hall29. Beyond Hall zero, joint literal installation remains an additional
check; this report proves neither automatic sufficiency nor a strict
counterexample to it.
