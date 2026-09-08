# Section 17 port substitution: final theorem audit

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

The corrected Section 17 is sound at its main theorem:
\(D_r\)-port-transversality is necessary and sufficient for the stated
closed, row-wise context substitution. The exact \(X\)-state and
\(Y\)-union ledgers are correct.

Ordinary \(D_r\)-transversality is insufficient, as Proposition 17.0 now
states. The hidden condition is not merely that a wreath contain its
selected Dyck set \(P\), but that its unique \(\infty\)-cut edge be

\[
 \{P,J\setminus P\}.
\tag{0.1}
\]

The currently known \(r=4\) nonlocal Haar packet does not preserve this
interface in its certified labelling. An explicit changed wreath loses
its Dyck port. Thus that packet cannot presently serve as the
noncanonical library member proposed after Corollary 17.2.

## 1. Exact cut structure and ownership ledgers

Let \(C\) be one minimum odd cycle in
\(KG(J\sqcup\{\infty\},r)\), where \(|J|=2r\).
Represent its wreath by a cyclic coordinate order and rotate that order
to

\[
 (\infty,j_1,j_2,\ldots,j_{2r}).
\tag{1.1}
\]

The \(r+1\) length-\(r\) windows avoiding \(\infty\) are

\[
 X_t=\{j_{t+1},\ldots,j_{t+r}\},
 \qquad 0\le t\le r.
\tag{1.2}
\]

### Lemma 1.1 (one-wreath port ledger)

The sequence in (1.2) is a Johnson geodesic and

\[
 X_r=J\setminus X_0.
\tag{1.3}
\]

For \(0\le t<r\), define

\[
 Y_t=X_t\cup X_{t+1},
\qquad
 Z_t=\{\infty\}\cup(J\setminus Y_t).
\tag{1.4}
\]

Then \(Z_0,\ldots,Z_{r-1}\) are exactly the wreath vertices containing
\(\infty\), and

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{r-1},X_r
\tag{1.5}
\]

is its Kneser-cycle order.

#### Proof

Consecutive \(X_t\) delete \(j_{t+1}\) and insert
\(j_{t+r+1}\), proving Johnson adjacency. The first and last windows are
the two complementary \(r\)-blocks of \(J\), proving (1.3).

Moreover

\[
 Y_t=\{j_{t+1},\ldots,j_{t+r+1}\}.
\]

Its complement in \(J\), together with \(\infty\), is the cyclic
length-\(r\) window crossing the cut in (1.1). These are all \(r\)
windows containing \(\infty\). Each \(Z_t\) is disjoint from both
neighbouring \(X\)-sets, giving (1.5). \(\square\)

### Lemma 1.2 (factor-wide exact ledgers)

Let \(G\) be any exact \(C_{2r+1}\)-factor. Cutting every wreath at its
actual \(\infty\)-ports gives

\[
 \biguplus_{C\in G}\biguplus_{t=0}^{r}\{X_t(C)\}
 =\binom Jr
\tag{1.6}
\]

and

\[
 \biguplus_{C\in G}\biguplus_{t=0}^{r-1}\{Y_t(C)\}
 =\binom J{r+1}
\tag{1.7}
\]

as multisets.

#### Proof

The left side of (1.6) is exactly the collection of factor vertices
avoiding \(\infty\), each owned once. The map

\[
 Y\longmapsto\{\infty\}\cup(J\setminus Y)
\tag{1.8}
\]

is a bijection from \(\binom J{r+1}\) to the
\(\infty\)-containing \(r\)-sets. Lemma 1.1 identifies this map with
\(Y_t\mapsto Z_t\), and exact ownership of the \(Z_t\) proves (1.7).
\(\square\)

These ledgers use exact factor multiplicity. They are true independently
of any Dyck transversal. What the transversal controls is the row-wise
boundary attachment.

## 2. Why the port condition is exact

For a wreath \(C\), write

\[
 \partial_\infty C=\{A_C,J\setminus A_C\}
\tag{2.1}
\]

for the endpoints of its \(\infty\)-deleted Johnson path.

### Theorem 2.1 (necessary and sufficient interface)

Let an aligned size-\(r\) hole have fixed exterior state \(O\), local
coordinate set \(J\), and canonical boundary rows

\[
 O\cup P,\qquad O\cup(J\setminus P),
\qquad P\in D.
\tag{2.2}
\]

Replacing one canonical row by the complete \(\infty\)-cut trace of one
wreath of an exact local factor \(G\), while leaving all outer row pieces
fixed, is possible for every row if and only if

\[
 |D\cap\partial_\infty C|=1
\qquad(C\in G).
\tag{2.3}
\]

Under (2.3), both discrepancies in (13A.5) vanish and the ambient factor
remains exact.

#### Proof

Assume (2.3). The selected ports are distinct factor vertices. Since

\[
 |G|={1\over2r+1}\binom{2r+1}{r}
 =\operatorname{Cat}_r=|D|,
\tag{2.4}
\]

they enumerate \(D\) exactly once. Orient the cut path of the wreath
assigned to \(P\) from \(P\). Lemma 1.1 gives

\[
 P=X_0,X_1,\ldots,X_r=J\setminus P.
\tag{2.5}
\]

Thus both states in (2.2) are fixed in their original row. Lemma 1.2
shows that the new local state and union multisets are respectively
\(\binom Jr\) and \(\binom J{r+1}\), exactly as for the canonical local
factor. Since \(O\cap J=\varnothing\) and \(O\) is fixed,

\[
 (O\cup X_t)\cup(O\cup X_{t+1})=O\cup Y_t.
\]

Hence both ledgers (13A.5) vanish. The fixed row endpoints leave the two
outer incident edges unchanged, and Theorem 13A.2 applies.

Conversely, suppose one wreath supplies the row with boundary pair
\((P,J\setminus P)\). Both boundary sets must occur in its
\(\infty\)-cut trace. They are disjoint. Among the \(r+1\) windows in
(1.2), the only disjoint pair is the endpoint pair. Therefore

\[
 \partial_\infty C=\{P,J\setminus P\}.
\]

Every row must be supplied once, so (2.3) follows. \(\square\)

Equivalently, \(G\) must contain the prescribed cut-edge matching

\[
 M_D=\bigl\{\{P,J\setminus P\}:P\in D\bigr\}.
\tag{2.6}
\]

This formulation makes the rooting issue completely explicit.

## 3. Minimal failure of ordinary transversality

For \(r=2\), take \(J=\{1,2,3,4\}\), \(\infty=0\), and

\[
 D=\{23,24\}.
\]

The coordinate cycles

\[
 (0,1,2,3,4),\qquad(0,2,4,1,3)
\tag{3.1}
\]

form an exact Petersen \(C_5\)-factor and each contains exactly one member
of \(D\). Thus ordinary \(D\)-transversality holds.

The first cycle, however, leaves the Johnson path

\[
 12-23-34
\tag{3.2}
\]

after deleting the \(0\)-containing windows. Its ports are \(12,34\);
the selected Dyck set \(23\) is interior, and its complement \(14\) is
not on this path. Reversal gives \(34-23-12\) and does not repair the
root. This is the minimal counterexample because at \(r=1\) both
\(\infty\)-avoiding singleton windows are ports.

The aggregate ledgers of Lemma 1.2 remain correct in this example. The
two cut paths are

\[
 12,23,34
 \qquad\text{and}\qquad
 24,14,13.
\]

Their \(X\)-multiset is all six members of \(\binom J2\), while their
adjacent unions are

\[
 123,234,124,134,
\]

all four members of \(\binom J3\). The failure is solely that these exact
aggregate ledgers cannot be attached to the old outer collars row by row.

## 4. Hidden interface assumptions

The corrected theorem uses all of the following.

1. The distinguished local coordinate \(\infty\) is fixed by the outer
   context. Changing it changes the ports.
2. The inherited relabelling must preserve the ordered boundary pair
   \(P,J\setminus P\), not merely the set of Dyck roots.
3. The exterior \(O\) is constant throughout the slab and disjoint from
   \(J\).
4. The slab contains all \(r+1\) state cells and all \(r\) internal
   adjacent-union cells of the replacement path.
5. Its two endpoint states are fixed in each row. Endpoint multiset
   equality is insufficient because each endpoint remains coupled to its
   unchanged outside collar.
6. Reversal is not an independent interface choice: once the ordered
   entrance state is fixed, the orientation in (2.5) is forced.
7. Simultaneous substitutions must have disjoint changed state and edge
   cells, or meet only in endpoint cells fixed by every participating
   substitution.
8. The two ownership equalities are multiset equalities. Support equality
   does not suffice.
9. Each new row is one complete \(\infty\)-cut trace of one wreath.  The
   necessity direction does not cover inter-wreath splicing, a permutation
   of exterior collars, or a separate endpoint-routing network; any of
   those would require an additional connector theorem and its own ledgers.

With these assumptions, the corrected Theorem 17.1 and the middle-levels
path-factor normal form in Theorem 17.3 are valid.

## 5. Which known constructions preserve ports?

### 5.1 Boundary-closed rectangle trades

The canonical MSW local factor is \(D_r\)-port-transversal by
construction. More generally, every exact local trade which fixes

\[
 P\quad\text{and}\quad J\setminus P
\]

in each affected row preserves the matching \(M_D\), hence preserves
port-transversality. Therefore the boundary-closed rectangles of
Section 13A and their phase-disjoint compositions preserve the ports of
the parent hole in which they are installed.

This does not imply that they preserve the ports of a nested child hole:
Theorem 13A.3 works precisely by changing a child entrance state. Port
compatibility must be checked again at the child scale.

### 5.2 The certified \(r=4\) nonlocal Haar packet

The eight changed orders in NONLOCAL_HAAR_M4.md use the step-two window
convention

\[
 I_i^{(4)}(q)=\{q_i,q_{i+2},q_{i+4},q_{i+6}\}.
\tag{5.1}
\]

If \(\infty=9=q_s\), the two ports are

\[
 I_{s+1}^{(4)}(q),\qquad I_{s+2}^{(4)}(q).
\tag{5.2}
\]

In the standard size-four Dyck interface, a sorted set
\(P=\{p_1<p_2<p_3<p_4\}\subset[8]\) is in \(D_4\) exactly when

\[
 p_i\le2i-1\qquad(1\le i\le4).
\tag{5.3}
\]

Consider the first negative and positive changed orders:

\[
 q^-=(1,8,6,7,4,5,3,9,2),
\tag{5.4}
\]

\[
 q^+=(1,9,3,5,4,7,6,8,2).
\tag{5.5}
\]

For \(q^-\), formula (5.2) gives the complementary ports

\[
 \{1,3,4,6\},\qquad\{2,5,7,8\}.
\tag{5.6}
\]

The first set satisfies (5.3), so this changed wreath has a \(D_4\)-port.
For \(q^+\), the ports are

\[
 \{1,5,7,8\},\qquad\{2,3,4,6\}.
\tag{5.7}
\]

The first violates \(p_2\le3\), while the second omits \(1\). Thus the
positive wreath has no \(D_4\)-port.

Consequently the certified four-for-four Haar packet does not preserve
the standard port matching under its given labelling. In particular its
positive exact-factor side, which contains \(q^+\), is not
\(D_4\)-port-transversal for this interface.

This does not rule out a different pre-embedding coordinate permutation
or a different completion whose complete port family is the inherited
\(D_4\). That is a new finite construction requirement; it is not proved
by the existing middle- and first-shadow cancellations.

## 6. Consequence for the replacement-seed lane

Corollary 17.2 is valid only with a library of parent factors satisfying
the port condition (2.3). Retaining the same ordinary Dyck transversal
is not enough.

The current unconditional boundary is therefore:

1. the corrected port-substitution theorem is proved;
2. canonical and row-boundary-closed parent trades preserve ports;
3. the certified nonlocal \(r=4\) Haar packet fails the standard port
   interface in its existing labelling;
4. no sufficiently rich \(D_{r+1}\)-port-transversal library whose rooted
   profiles meet the packet-capacity bound of Corollary 17.2 is presently
   proved.

Thus the local seed problem is exactly a rooted complement-path-factor
problem in the middle-levels graph, as Theorem 17.3 states. Exact shadow
cancellation without the prescribed endpoint matching does not solve it.

## 7. Adversarial audit

1. The proof does not infer port compatibility from aggregate \(X/Y\)
   ownership.
2. Formula (5.2) accounts for the step-two convention in the Haar
   certificate; using four consecutive displayed entries would be wrong.
3. One failed wreath is enough to disprove port-transversality of a
   completed factor.
4. The negative statement about the Haar packet is for its certified
   labelling and the standard inherited \(D_4,\infty=9\) interface. No
   impossibility under every independent re-embedding is claimed.
5. The corrected theorem permits no silent permutation of outer row
   collars. A construction allowing such a permutation would need a
   separate connector theorem and new boundary ledgers.
