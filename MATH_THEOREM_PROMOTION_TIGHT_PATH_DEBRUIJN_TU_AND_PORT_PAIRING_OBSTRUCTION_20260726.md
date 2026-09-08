# Promotion tight-path covers: safe de Bruijn flow, determinant two, and the port-pairing obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},
\tag{0.1}
\]

at the tuned height

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=(1+o(1))\frac Wm.
\tag{0.2}
\]

The rigid requirement “one tight Hamilton cycle at every root” can be
weakened substantially. If root \(A\) uses \(c_A\) tight promotion
paths/cycles, then cutting cycles and inserting collars costs

\[
                         O\!\left(H\sum_A c_A\right).
\tag{0.3}
\]

Consequently either of the bounds

\[
 \max_A c_A=O(\log m)
 \quad\text{or, more generally,}\quad
 \sum_Ac_A=o(W/H)
\tag{0.4}
\]

has \(o(W)\) total collar toll. Since \(N_H\sim W/m\), the uniform
condition \(c_A=o(m/H)\) implies the second bound.

Indeed, if \(c_A\le k\), then

\[
 H\sum_Ac_A\le HkN_H=(1+o(1))W\frac{Hk}{m}.
\tag{0.4a}
\]

For \(k=O(\log m)\), the final ratio is
\(O((\log m)^{3/2}/\sqrt m)=o(1)\); for \(k=o(m/H)\), it is \(o(1)\)
by definition.

This note gives the exact flow model for this relaxation and a decisive
integrality audit.

1. Ordered \(H\)-sets are arcs of the injective de Bruijn digraph on
   ordered \((H-1)\)-tuples. This is correct for the middle layer.

2. It is not enough for a literal two-sided compiler. To expose flags
   through depth \(d\), the state must remember an injective word of
   length
   \[
                            \ell=H+d.
   \tag{0.5}
   \]
   In particular the full radius-\(H\) collar needs \(2H\)-letter
   safety. The \(H\)-memory graph admits internal returns which collapse
   the upper union rank.

3. With the corrected memory, the root-local conservation block is an
   ordinary network matrix (node capacities have the standard split-node
   network extension). The exact root arc-count and component budgets are
   separate side constraints. Even before those rows are imposed,
   adjoining the global middle-target capacities destroys total
   unimodularity. For every
   \(2\le d\le H\), the coupled state-incidence/target matrix contains a
   square minor of determinant \(2\), already inside one root.

4. Splitting a target into a capacity-one network node restores a
   network only by forgetting which ordered occurrence entered the
   target. Flow may enter through occurrence \(e\) and leave through
   occurrence \(f\). The physical system requires the same occurrence,
   or a specifically certified bridge-one port pair. This is the exact
   pairing constraint which destroys the network formulation.

5. The tempting cross-root pairing is not physical. A bridge-one
   transition which preserves the middle owner also preserves the collar
   top. Hence two occurrences of the same target belonging to different
   roots cannot be spliced at that target. Known transparent root/frame
   switches require two synchronized paths and an \(H+1\)-step tail; they
   are nonlocal rectangle gadgets, not target-node flow.

Thus the bounded-component relaxation is valid and potentially useful,
but target capacity plus root-local circulation is not TU. The surviving
gate is a **colored safe-de-Bruijn path cover with diagonal port pairing
and \(o(W/H)\) components**. It is weaker than one Hamilton cycle per
root, but it remains a genuine globally coupled integral problem.

## 1. Complement-root convention

A root is

\[
                         A\in\binom V{m-H},
\qquad U=A^c,\qquad |U|=M.
\tag{1.1}
\]

For an \(H\)-set \(J\subset U\), use the complement-form middle target

\[
                         D=A\cup J.
\tag{1.2}
\]

Its complement \(X=V\setminus D=U\setminus J\) is the literal middle
owner in the promotion-ring convention. Thus capacity one on the
\(D\)'s is exactly capacity one on the literal owners.

If

\[
 J_i=\{z_i,z_{i+1},\ldots,z_{i+H-1}\},
\tag{1.3}
\]

then consecutive complements \(X_i=U\setminus J_i\) are the ordinary
fixed-top bridge-one promotion steps. Hence a tight path in the \(J\)'s
is a literal promotion path after complementation.

## 2. The safe de Bruijn state graph

Fix a protected depth \(0\le d\le H\) and put

\[
                         \ell=H+d.
\tag{2.1}
\]

For a root \(A\), define \(\mathcal B_{A,d}\) as follows.

- A vertex is an injective ordered \((\ell-1)\)-tuple from \(U=A^c\).
- An arc is an injective ordered \(\ell\)-tuple
  \[
                         e=(z_0,z_1,\ldots,z_{\ell-1}).
  \tag{2.2}
  \]
- Its tail and head are
  \[
  t(e)=(z_0,\ldots,z_{\ell-2}),\qquad
  h(e)=(z_1,\ldots,z_{\ell-1}).
  \tag{2.3}
  \]
- Its middle colour is
  \[
                         \kappa_0(e)
  =A\cup\{z_0,\ldots,z_{H-1}\}.
  \tag{2.4}
  \]

For \(0\le q\le d\), define the two signed flag colours

\[
 \kappa_q^-(e)
 =A\cup\{z_q,z_{q+1},\ldots,z_{H-1}\},
\tag{2.5}
\]

\[
 \kappa_q^+(e)
 =A\cup\{z_0,z_1,\ldots,z_{H+q-1}\}.
\tag{2.6}
\]

They have ranks \(m-q\) and \(m+q\), respectively. Complementing swaps
the two signs but changes none of the capacity questions.

### Proposition 2.1 (safe-path literalization)

Let \(e_0,e_1,\ldots,e_{s-1}\) be a directed path in
\(\mathcal B_{A,d}\). Then its middle colours are a tight path of
distinct-position \(H\)-windows, and (2.5)--(2.6) are exactly the
intersection and union flags of \(q+1\) consecutive middle windows for
every \(q\le d\).

Conversely, every fixed-root promotion word whose every
length-\((H+d)\) block is injective gives such a path.

#### Proof

The overlap equation \(h(e_i)=t(e_{i+1})\) produces one underlying word

\[
                         z_0,z_1,\ldots,z_{H+d+s-2}.
\tag{2.7}
\]

The middle set at phase \(i\) is its length-\(H\) window. The
intersection of the windows at phases \(i,\ldots,i+q\) is

\[
                         \{z_{i+q},\ldots,z_{i+H-1}\},
\tag{2.8}
\]

and their union is

\[
                         \{z_i,\ldots,z_{i+H+q-1}\}.
\tag{2.9}
\]

Injectivity of every length-\((H+d)\) block makes (2.8)--(2.9) have
sizes \(H-q\) and \(H+q\). Adding \(A\) gives (2.5)--(2.6). The converse
is the same construction read backwards. \(\square\)

### Proposition 2.2 (\(H\)-memory is insufficient)

For every \(1\le q\le H\), the injective \(H\)-word de Bruijn graph
contains a directed path whose middle \(H\)-windows are legal but whose
depth-\(q\) upper union has size less than \(H+q\).

#### Proof

Choose a word

\[
 z_0,z_1,\ldots,z_{H+q-1}
\tag{2.10}
\]

such that every \(H\) consecutive entries are distinct but

\[
                         z_{H+q-1}=z_0.
\tag{2.11}
\]

This is possible because the two repeated positions are separated by
\(H+q-1\ge H\); take every other entry distinct. The corresponding
length-\(H\) windows are arcs of the \(H\)-memory graph. Their union
through phase \(q\) is the set of entries in (2.10), which has at most
\(H+q-1\) elements. It therefore cannot be a rank-\((m+q)\) flag.
\(\square\)

So the proposed ordered-\(H\)-set circulation is a middle-only
relaxation. The corrected literal graph is \(\mathcal B_{A,d}\), with
\(d=H\) for a full Gaussian collar.

## 3. The bounded-component integer system

For every arc \(e\in E(\mathcal B_{A,d})\), introduce

\[
                         y_e\in\{0,1\}.
\tag{3.1}
\]

The natural constraints are:

### Root-local state constraints

\[
 \sum_{e:t(e)=v}y_e\le1,\qquad
 \sum_{e:h(e)=v}y_e\le1
 \qquad(v\in V(\mathcal B_{A,d})),
\tag{3.2}
\]

with prescribed divergence

\[
 \sum_{e:t(e)=v}y_e-\sum_{e:h(e)=v}y_e=b_{A,v}.
\tag{3.3}
\]

For a repaired root quota one asks for

\[
                         \sum_{e\in E(\mathcal B_{A,d})}y_e=M-1.
\tag{3.4}
\]

### Global target capacities

At the middle,

\[
 \sum_{\substack{A,e\\\kappa_0(e)=D}}y_e\le1
 \qquad\left(D\in\binom Vm\right).
\tag{3.5}
\]

If literal band disjointness is imposed, add

\[
 \sum_{\substack{A,e\\\kappa_q^\pm(e)=T}}y_e\le1
\tag{3.6}
\]

for every protected signed target \(T\) and \(q\le d\), with the usual
small capacity clones when the scalar occurrence count exceeds the
layer size by \(o(W)\).

The conservation equations (3.3), bounds, and node capacities have the
standard split-node network extension and are integral for fixed integral
supplies. The cardinality equation (3.4) is an additional length side
constraint; it is not asserted to preserve TU in the displayed
arc-variable matrix. An integral solution of (3.2)--(3.3) is a disjoint
union of directed paths and cycles at every root. Cutting each cycle once
turns it into promotion paths.

The state equations alone do not control the number of cycle
components. Thus the exact sufficient condition includes the separate
component bound

\[
                         \sum_A c_A=o(W/H).
\tag{3.7}
\]

Under (3.5)--(3.7), and the appropriate near-SCD tag census, the usual
bridge-one compiler has only \(o(W)\) target appendage and collar cost.
This proves that a bounded tight-path cover is a genuine weakening of one
Hamilton cycle per root.

## 4. Target capacity destroys total unimodularity

Let \(B\) be the block-diagonal directed node--arc incidence matrix of
the graphs \(\mathcal B_{A,d}\), and let \(C\) be the middle-colour
matrix from (3.5).

### Theorem 4.1 (safe determinant-two minor)

For every \(2\le d\le H\) and all sufficiently large \(m\), the matrix

\[
                         \begin{pmatrix}B\\C\end{pmatrix}
\tag{4.1}
\]

contains a square submatrix of determinant \(\pm2\). Consequently the
target-capacitated safe-circulation system is not totally unimodular.
The obstruction occurs inside a single root.

#### Proof

Fix one root \(A\), put \(\ell=H+d\), and choose pairwise distinct labels

\[
 a_0,\ldots,a_{H-1},\quad
 c_1,\ldots,c_d,\quad
 f_1,\ldots,f_{d+1}
\tag{4.2}
\]

in \(U=A^c\). This uses \(H+2d+1\le3H+1<M\) labels for all sufficiently
large \(m\).

Consider the cyclic word of length

\[
                         L=2\ell+1
\tag{4.3}
\]

given by

\[
 a_0,a_1,\ldots,a_{H-1},
 c_1,\ldots,c_d,
 a_0,a_1,\ldots,a_{H-1},
 f_1,\ldots,f_{d+1}.
\tag{4.4}
\]

The two copies of each \(a_j\) are at cyclic distances \(\ell\) and
\(\ell+1\). Hence every cyclic length-\(\ell\) block is injective, so
the \(L\) consecutive blocks are arcs of \(\mathcal B_{A,d}\) forming a
directed cycle. Their ordered \((\ell-1)\)-state vertices are distinct:
equality of two such states forces equality of their first labels.
Every filler label has a unique occurrence. The only remaining case is
the pair of starts at the two copies of some \(a_j\); before the
\((\ell-1)\)-blocks end, one encounters a \(c\)-label in the first block
and an \(f\)-label in the second, because \(d\ge2\).

Put

\[
                         J=\{a_0,\ldots,a_{H-1}\},
\qquad D=A\cup J.
\tag{4.5}
\]

Exactly two arcs of this directed cycle have middle colour \(D\): the
arcs starting at the two displayed copies of \(a_0\). Every other
length-\(H\) initial block contains a \(c_i\) or an \(f_i\).

Take all \(L\) arc columns, delete one row from the node--arc incidence
matrix of this directed \(L\)-cycle, and append the target row \(D\).
The deleted incidence matrix has rank \(L-1\), and its one-dimensional
right kernel is spanned by the all-ones vector. Therefore the determinant
of the resulting \(L\times L\) matrix is, up to sign, the sum of the
entries of the target row around the cycle. That sum is \(2\).
\(\square\)

The theorem persists after all entrance, tag, quota, endpoint, and
component rows are appended, because the displayed minor is already
present after row deletion. It also persists with the correct
two-sided \(2H\)-memory, by taking \(d=H\).

### Corollary 4.2 (literal fractional circulation gap)

On the directed cycle (4.4), the assignment

\[
                         y_e=\frac12
\tag{4.6}
\]

on every cycle arc is a nonzero fractional circulation satisfying the
capacity-one row of \(D\). There is no nonzero integral circulation
supported on the same cycle and satisfying that row.

#### Proof

Conservation on a directed cycle forces every arc to have one common
value \(\alpha\). The target \(D\) occurs twice, so its capacity is
\(2\alpha\le1\). Thus \(\alpha=1/2\) is fractionally feasible. For an
integral circulation, \(\alpha\in\{0,1\}\); the value \(1\) violates the
target row, leaving only zero. \(\square\)

Allowing open paths can escape this particular trap only by omitting at
least one of the two \(D\)-coloured arcs. This creates a path boundary
and a one-unit root-quota deficit which must be replaced elsewhere.
Hence the corollary is an exact statewise integrality obstruction, not by
itself a lower bound on the minimum global component count.

### Remark 4.3 (what the minor means)

For a directed cycle, ordinary circulation permits any scalar multiple
of its all-ones arc vector. The target row cuts that cycle twice. The
resulting parity-two intersection is exactly what a network incidence
matrix cannot represent. This is the path-cover analogue of the
determinant-two packet minor, but it survives after replacing one
Hamilton packet by arbitrary safe tight paths and cycles.

## 5. Why target-node splitting is not a physical repair

There is a tempting extended formulation. For every ordered occurrence
\(e\) of a target \(D\), split the arc into

\[
 t(e)\longrightarrow D\longrightarrow h(e),
\tag{5.1}
\]

put capacity one at \(D\), and join all roots through the same target
node. The result is an ordinary network and is integral.

It is not equivalent to (3.5).

Let \(e^{\rm in}\) and \(e^{\rm out}\) be the two halves of occurrence
\(e\). The physical diagonal equations are

\[
                         y_{e^{\rm in}}=y_{e^{\rm out}}
 \qquad(e\text{ an ordered occurrence}),
\tag{5.2}
\]

together with

\[
                         \sum_{e:\kappa_0(e)=D}y_e\le1.
\tag{5.3}
\]

An ordinary target node retains only

\[
 \sum_{e:\kappa_0(e)=D}y_{e^{\rm in}}
 =
 \sum_{e:\kappa_0(e)=D}y_{e^{\rm out}}
 \le1.
\tag{5.4}
\]

It may pair the incoming half of occurrence \(e\) with the outgoing half
of a different occurrence \(f\). Thus it forgets both the root and the
ordered overlap state. Equations (5.2) are precisely the missing port
pairing.

### Theorem 5.1 (same-target root switching is not bridge-one)

Let two complete radius-\(H\) useful states have the same middle owner
but different collar tops, equivalently different roots in the
complement convention. There is no bridge-one arc between them.

#### Proof

The complete bridge-one classification has three cases.

1. Identity preserves the owner and the collar top.
2. A rotor shift changes the middle owner by a nontrivial Johnson move.
3. A promotion can preserve the middle owner, but every promotion
   preserves the collar top.

Therefore a bridge-one arc preserving the owner also preserves the top.
Different complement roots mean different tops, so no such arc exists.
\(\square\)

Even within one root, (5.4) is too permissive: same-owner promotions
realize only the specific move-to-front port pairs in the bridge-one
classification, not the complete bipartite pairing of all incoming and
outgoing ordered occurrences.

Hence root switching cannot be used to turn the target capacities into
ordinary single-commodity flow.

## 6. What physical switching remains available

There are literal root/frame-changing surgeries, but they do not occur
at one target node. The transparent pairing two-switch uses

1. two simultaneous bridge-one paths;
2. conjugate entrance states;
3. synchronized tails through time \(H+1\); and
4. a four-coordinate frame switch.

It exchanges the two tails, preserves their middle-owner multiset, and
returns to the original frame after the synchronized collar. Thus it can
be used as a nonlocal absorber without increasing the component count.

Algebraically, however, this is a two-path rectangle variable. It couples
two target occurrences and \(H+1\) consecutive state transitions. It is
not a legal pairing edge at the single node \(D\), and adjoining such
rectangle variables does not remove the determinant-two minor of
Theorem 4.1 unless one proves a separate global decomposition into
transparent rectangles.

So physical switching remains a possible construction tool, but not a
TU explanation.

## 7. Exact surviving reduction

For a protected depth \(d\), define the **safe coloured path-cover gate**
\(\operatorname{SCP}(d)\) as the existence of an integral arc set in
\(\bigsqcup_A\mathcal B_{A,d}\) satisfying:

1. root quota \(M-1\), up to total \(o(W)\) quarantine;
2. root-local state balance with path/cycle decomposition;
3. total component count \(o(W/H)\);
4. middle repeat excess and holes \(o(W)\);
5. aggregate signed flag holes through the required depths \(o(W)\); and
6. the diagonal occurrence pairing (5.2), or an explicitly certified
   replacement by transparent multi-path switches.

### Theorem 7.1 (conditional bounded-path compiler)

If \(\operatorname{SCP}(H)\) holds with the calibrated tag census, then
the promotion-ring lane gives a literal word of length \(W+o(W)\).

The same implication holds for a fixed entrance depth \(d=o(H)\), with
the already audited outer-band and tail compiler appended.

#### Proof

Proposition 2.1 gives literal bridge-one paths and their two-sided flags.
Items 1, 4, and 5 give \(W-o(W)\) useful occurrences and only \(o(W)\)
literal appendage. Cut every selected cycle once. By item 3 and (0.3),
all resets and collars cost \(o(W)\). The tag census supplies the
correct active depths, and the outer compiler has \(o(W)\) cost by
hypothesis. Summing the ledgers gives \(W+o(W)\). \(\square\)

### Theorem 7.2 (integrality boundary)

After target colours, the root cardinality rows, and the component budget
are deleted, the remaining conservation system is a product of integral
network-flow systems. Restoring the target colours alone already makes
the natural matrix non-TU by Theorem 4.1. Contracting targets to recover
a network is not physical by Theorem 5.1. The root arc-count and
low-component requirements are additional side constraints, not hidden
consequences of TU.

Therefore the bounded-path relaxation does not reduce the constant-one
gate to Hoffman circulation or ordinary max flow. Its exact residual is
the colored diagonal-port pairing plus low-component rounding.

## 8. Audited boundary

Proved here:

1. the exact safe-memory lift from \(H\) to \(H+d\);
2. the literal two-sided flag formulas for safe tight paths;
3. the \(o(W)\) collar criterion for bounded components;
4. the target-capacitated root-local flow formulation;
5. a determinant-two minor surviving at every \(2\le d\le H\);
6. the exact diagonal port-pairing constraint lost by target-node
   splitting;
7. the no-go for same-target cross-root bridge-one switching; and
8. the conditional bounded-path compiler.

Not proved here:

1. an integral \(\operatorname{SCP}(d)\) solution;
2. \(O(\log m)\) or \(o(m/H)\) components per root;
3. a transparent-rectangle decomposition of the fractional flow; or
4. coefficient one.

The useful conclusion is a sharp reduction/no-go. One Hamilton cycle per
root is unnecessary, but the proposed de Bruijn relaxation is not an
ordinary network once literal target ownership is restored. The exact
obstruction is not scalar capacity: it is the requirement that every
capacity-one target preserve its root-and-order occurrence port.

## 9. Dependency ledger

The calibrated packet-flow TU boundary is compared with
MATH_ATTACK_CALIBRATED_PACKET_FLOW_TRANSPORT_INTEGRALITY_20260725.md.
The exact bridge-one owner/top dynamics used in Theorem 5.1 are recorded
in MATH_ATTACK_EP_PROMOTION_BACKBONE_20260725.md and
MATH_ATTACK_EP_TAGH_COMMON_BASE_RECURSIVE_AUDIT_20260725.md.
The nonlocal legal switch in Section 6 is
MATH_ATTACK_CP_TRANSPARENT_PAIRING_TWOSWITCH_20260725.md.
The block-correlation lower bound remains
MATH_THEOREM_PROMOTION_RING_BLOCK_FACTOR_HOLE_FLOOR_20260726.md.
