# Audit of the ballot functional-cycle supply and the strand gate

Date: 2026-07-26

Method: pure mathematics only.  No finite search, solver, program, or web
input is used.

Audited sources:

* `MATH_THEOREM_TWISTED_PORT_MONODROMY_COMPOSITION_20260726.md`,
  especially corrected Section 3.6;
* `MATH_THEOREM_C6_C8_STRAND_SPLICING_20260726.md`;
* `MATH_THEOREM_BALLOT_FORCED_C8_SUFFIX_ROUTER_BANK_20260726.md`;
* `MATH_ATTACK_O_PHASE_MONODROMY_TWISTED_PORT_SERIAL_SIGN_20260726.md`.

## 0. Verdict

The ballot enumeration is correct:

\[
 Z_r=\frac{r-1}{r+2}\binom{2r}{r-1}
    =\frac{r(r-1)}{r+2}C_r.                           \tag{0.1}
\]

Every one of these \(Z_r\) cores has a directed cycle in the functional
digraph of the outgoing perfect matching.  The greedy lower bound

\[
 \frac{Z_r}{r(r+1)}
 =\frac{r-1}{(r+1)(r+2)}C_r                           \tag{0.2}
\]

is valid for pairwise selected-edge-disjoint **outgoing-matching cycle
certificates**.

The uncorrected implication from (0.1) to full-factor alternating switches
is false.  A proposed cross edge can already be the selected incoming
edge of the old path factor.  An exact \(r=2\) factor has the unique
ballot-forced raw \(C_6\) certificate and no admissible \(C_6/C_8\)
switch at all.  Thus the arbitrary-factor lower bound for admissible
cycles is exactly the trivial bound zero.

For the canonical MSW factor there is nevertheless an independent
positive abstract bank: \(C_{r-3}\) pairwise row-disjoint clean star
\(C_8\)'s, affecting \((1/16+o(1))C_r\) rows.  Their cut phases are mixed
and their new row lengths are \(r,r+2,r-1,r-1\).  They are valid
factor-alternating open-path routers, but they are not physical
fixed-exterior wreath packets.  Their port displacements
\((1,1,1,2)\) also rule out one common moving exterior.

Accordingly the exact boundary is:

\[
\boxed{
\begin{array}{c}
\text{raw ballot cycle supply: proved;}\\
\text{positive abstract canonical star-}C_8\text{ bank: proved;}\\
\text{ordinary fixed-exterior physical supply: zero;}\\
\text{row-dependent exterior-moving packet: open.}
\end{array}}                                           \tag{0.3}
\]

## 1. The ballot count

Orient an exact \(\mathcal D_r\)-port path factor from each Dyck root to
its barred terminal.  Let \(M^\uparrow\) contain the outgoing incidence
edge from every nonterminal lower state.  Each upper vertex has one
predecessor, so

\[
 M^\uparrow:\binom{[2r]}r\setminus\overline{\mathcal D_r}
                    \longrightarrow\binom{[2r]}{r+1}               \tag{1.1}
\]

is a perfect matching.

Fix an \((r-1)\)-set \(K\), encoded as a word with \(r-1\) up-steps and
\(r+1\) down-steps.  An extension \(K+a\) is a barred Dyck port exactly
when changing the down-step at \(a\) to an up-step produces a nonpositive
balanced path.

### Lemma 1.1

Such an extension exists if and only if the deficient path of \(K\) is
itself nonpositive.

#### Proof

If the changed path is nonpositive, the old path agrees with it before
\(a\) and is two units below it afterwards, hence is nonpositive.

Conversely, suppose the old deficient path is nonpositive.  Change the
down-step immediately after its last visit to height \(-1\).  Afterwards
the old height is at most \(-2\); the changed suffix is two units higher
and remains nonpositive, while the final height becomes zero.  \(\square\)

The ballot/reflection count of nonpositive deficient paths is

\[
 \binom{2r}{r-1}-\binom{2r}{r-2}
 =\frac3{r+2}\binom{2r}{r-1}.                        \tag{1.2}
\]

Subtracting (1.2) from all cores gives (0.1).  Thus both the fraction
\((r-1)/(r+2)\) and every displayed Catalan conversion are valid.

## 2. What the eligible core actually forces

For an eligible core every extension \(K+a\) belongs to the domain of
\(M^\uparrow\).  Write

\[
 f_K(a)=b
 \quad\Longleftrightarrow\quad
 (K+a)(K+a+b)\in M^\uparrow.                          \tag{2.1}
\]

The functional graph of \(f_K\) has \(r+1\) vertices, no loop, and no
directed two-cycle: a two-cycle would use the same upper vertex
\(K+a+b\) twice in the matching.  Hence it has a directed cycle of length
between three and \(r+1\).

This proves a cycle against \(M^\uparrow\), not yet against the full
factor

\[
                         F=M^\uparrow\cup M^\downarrow.             \tag{2.2}
\]

## 3. The missing full-factor condition

Let

\[
 a_0\to a_1\to\cdots\to a_{\ell-1}\to a_0            \tag{3.1}
\]

be a directed cycle of \(f_K\), and put

\[
 X_i=K+a_i,qquad Y_i=K+a_i+a_{i+1}.                  \tag{3.2}
\]

Call arc \(i\) **blocked** when

\[
                         Y_iX_{i+1}\in M^\downarrow.                 \tag{3.3}
\]

Equivalently, the next lower state of \(X_i\) on its old oriented path is
\(X_{i+1}\).

### Theorem 3.1 (exact alternation/strand criterion)

The lift of (3.1) is an \(F\)-alternating \(C_{2\ell}\) if and only if
none of its arcs is blocked.  This is also equivalent to the selected
states \(X_i\) lying on pairwise distinct old root strands.

#### Proof

At \(Y_i\), the old factor uses its unique \(M^\uparrow\)-mate \(X_i\)
and its unique \(M^\downarrow\)-mate.  The proposed other half-edge
\(Y_iX_{i+1}\) is absent from \(F\) exactly when (3.3) fails.  This proves
the first equivalence.

If two distinct states \(K+a,K+b\) lie on one complementary Johnson
geodesic, their Johnson distance is one, so they occur at consecutive
phases.  Their intervening upper state is \(K+a+b\), and the earlier
state's functional arc points to the later one.  Hence the corresponding
cycle arc is blocked.  Conversely a blocked arc is literally two
consecutive states on one strand.  \(\square\)

Thus a genuine outgoing-functional cycle is automatically clean; folded
\(C_6\) routers cannot arise from this one matching orientation.

For \(\ell=3\), Theorem 3.1 gives the common-core star \(C_6\).  For
\(\ell=4\), it gives the star \(C_8\), never the octahedral type.  Nothing
in the functional-graph argument forces \(\ell\le4\).

## 4. Exact phase and length ledger

Suppose a clean cycle has selected outgoing edges at phases
\(t_0,\ldots,t_{\ell-1}\).  The new component which uses the prefix ending
at \(X_{i+1}\) and the suffix beginning at \(Y_i\) has incidence length

\[
                 2r+2(t_{i+1}-t_i).                  \tag{4.1}
\]

Consequently one open router has equal component lengths if and only if
all phases agree.  The shifts sum to zero around the endpoint orbit, but
this orbit-sum identity is only a formal variable-length ledger.

There are four distinct gates:

1. a directed \(M^\uparrow\)-cycle;
2. a full-factor alternating cycle (Theorem 3.1);
3. an equal-length open router (common phase in the clean case);
4. a physical minimum-wreath trade (joint identity endpoint monodromy and
   literal geodesicity, with all exterior collars).

The ballot theorem proves only Gate 1.

## 5. Exact counterexample to unconditional extraction

At \(r=2\), let \(\mathcal D_2=\{12,13\}\) and take the exact port factor

\[
 12-124-14-134-34,
 \qquad
 13-123-23-234-24.                                    \tag{5.1}
\]

The six lower states and four upper states occur exactly once, and the
displayed endpoints are the required complement pairs.

The unique eligible core is \(K=\{1\}\).  Its outgoing arcs are

\[
                         2\to4\to3\to2.               \tag{5.2}
\]

But \(124-14\) is already the old down-edge in the first path.  Hence
(5.2) is not an \(F\)-alternating \(C_6\).  The raw bank is nonempty and
the admissible \(C_6/C_8\) bank is empty.

This disproves every unconditional implication from (0.1)--(0.2) to a
positive strand-admissible subbank.

## 6. Why the raw averaging cannot repair the defect

For each upper vertex \(Y\), let \(X\) be its \(M^\uparrow\)-mate and
\(Z\) its \(M^\downarrow\)-mate.  The core \(K=X\cap Z\) is the unique
core in which the corresponding functional arc is blocked.  Therefore
blocked arcs over all cores are in bijection with upper vertices and
number

\[
             \binom{2r}{r+1}=inom{2r}{r-1}=rC_r.    \tag{6.1}
\]

On eligible cores, the terminal transition cannot contribute a blocker;
the sharper bound is \((r-1)C_r\).  It is still larger than \(Z_r\):

\[
               \frac{(r-1)C_r}{Z_r}=\frac{r+2}{r}>1. \tag{6.2}
\]

One blocked arc can destroy a whole functional cycle.  Thus the proved
budgets permit every eligible core to be contaminated.  A raw directed
cycle cannot have every arc blocked, since then both halves would form a
portless cycle component of the old factor, but this weaker fact gives no
toggle.

The raw cycle may also have length at least five or have mixed phase.
Neither defect is bounded by (0.1).

## 7. Correct conditional extraction theorem

Let \(\mathcal G\) be a set of eligible cores for which one has separately
proved a genuine alternating cycle \(C_K\) of length \(\ell_K\), with any
required phase condition.  Choose one such cycle per core.

An outgoing matching edge belongs to at most \(r\) core fibres.  Two
distinct \((r-1)\)-cores can share at most one selected matching edge.
Hence the conflict degree of \(C_K\) is at most
\(\ell_K(r-1)\).  Random priority, or the Caro--Wei bound, gives a
selected-edge-disjoint bank \(\mathcal B\) with

\[
 \boxed{
 |\mathcal B|\ge
 \sum_{K\in\mathcal G}\frac1{1+(r-1)\ell_K}.}        \tag{7.1}
\]

Selected-edge disjointness here implies incidence-vertex disjointness:
every lower cycle vertex contributes its unique outgoing edge, and every
upper cycle vertex is the upper endpoint of that edge.

In particular, if \(G_3\) good cores carry \(C_6\)'s and \(G_4\) further
good cores carry star \(C_8\)'s, then

\[
 |\mathcal B|\ge\frac{G_3}{3r-2}+\frac{G_4}{4r-3}.    \tag{7.2}
\]

For the coarser hypothesis \(\ell_K\le L\),

\[
 |\mathcal B|\ge\frac{|\mathcal G|}{1+L(r-1)}.        \tag{7.3}
\]

This bank may still cut different phases of the same old row.  A directly
switch-stable atlas needs a second extraction for old-strand disjointness.
The crude universal load bound gives \(|\mathcal G|/(4r^2)\) for short
cycles, whereas (7.2) gives \(|\mathcal G|/(4r)\) incidence-disjoint
cycles.  No unconditional theorem currently proves \(|\mathcal G|>0\).

## 8. Canonical positive abstract \(C_8\) bank

The failure of universal extraction does not mean that every factor has
zero good cycles.  In the canonical rank-three factor the four outgoing
edges

\[
 124-1246,quad146-1456,quad145-1345,quad134-1234    \tag{8.1}
\]

form the clean star cycle

\[
 124-1246-146-1456-145-1345-134-1234-124.             \tag{8.2}
\]

Its common core is \(\{1,4\}\), and its selected-edge phases are
\((0,2,1,0)\).  The four root strands are distinct, so Theorem 3.1 proves
full-factor alternation.

For \(r\ge3\), prefixing by a Dyck word \(A\) of semilength \(q\),
suffixing by a Dyck word \(B\) of semilength \(r-q-3\), and using MSW
concatenation suspends (8.2).  For fixed \(q\) this gives

\[
                         C_qC_{r-q-3}                 \tag{8.3}
\]

pairwise row- and vertex-disjoint clean star \(C_8\)'s at phases

\[
                         (q,q+2,q+1,q).               \tag{8.4}
\]

Taking \(q=r-3\) gives \(C_{r-3}\) routers and affects

\[
 \frac{4C_{r-3}}{C_r}
 =\frac{r(r-1)(r+1)}{2(2r-1)(2r-3)(2r-5)}
 \longrightarrow\frac1{16}                          \tag{8.5}
\]

of all rows.  The new row semilengths are

\[
                         r,quad r+2,quad r-1,quad r-1.           \tag{8.6}
\]

Thus (8.2)--(8.6) prove a positive-density **abstract open-path router
bank**, not a minimum-wreath packet bank.

## 9. Fixed-exterior and common-moving-exterior obstruction

Let a local rank-\(r\) boundary move from exterior \(O_L\) to \(O_R\),
and put \(e=|O_L\setminus O_R|\).  If its local endpoint label changes
from \(P\) to \(\tau(P)\), then

\[
 d_J\bigl(O_L\cup P,O_R\cup(J\setminus\tau(P))\bigr)
                          =e+|P\cap\tau(P)|.           \tag{9.1}
\]

Every contiguous segment of a minimum wreath is geodesic.  An ordinary
\(r\)-step slab therefore requires

\[
                          e=|P\setminus\tau(P)|.       \tag{9.2}
\]

Fixed exterior gives \(e=0\), so \(\tau(P)=P\) pointwise.  Nonidentity
twisted fixed-exterior slabs are impossible; a later inverse twist cannot
repair the earlier nongeodesic segment.

For the four-cycle (8.2), the port displacements are

\[
                            (1,1,1,2).                 \tag{9.3}
\]

Thus no single common exterior motion satisfies (9.2).  Using the actual
variable lengths (8.6) would require exterior motions

\[
                            (1,3,0,1),                 \tag{9.4}
\]

again not common.  The positive abstract bank therefore cannot be promoted
by one fixed or common-moving exterior.

## 10. Precise surviving gate

Theorem 3.6 supplies raw functional cycles, not physical trades.  The
canonical suffix construction supplies a positive-density clean abstract
\(C_8\) bank, but its unequal phase lengths and unequal port displacements
are a sharp strand/exterior obstruction.

A positive coefficient-one packet must now do all of the following in one
integral construction:

1. move exteriors rowwise so that (9.2) holds;
2. own every new exterior and crossing-collar \(X/Y\) resource exactly;
3. close the total endpoint monodromy inside the same joint geodesic
   packet; and
4. prove a favourable full carrier vector including the collars.

No current theorem proves such a packet.  The ordinary fixed-exterior
version is rigorously impossible.
