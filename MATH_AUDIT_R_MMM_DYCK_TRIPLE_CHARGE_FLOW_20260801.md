# Independent audit of the MMM Dyck-triple charge-flow theorem

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_R_MMM_DYCK_TRIPLE_CHARGE_FLOW_AND_FINITE_TRANSPORT_BASIS_20260801.md`  
Verdict: the six-filler block, corrected incidence operator, zero-sum charge,
Dyck-state connectivity, integral tree flow, and capacitated cut theorem are
valid with the scopes stated below.  The earlier proposed canonical
3-regular cover is false and is not retained.  Literal paired packet
transporters remain a hypothesis.

## 1. Audit protocol

The decisive statements were checked independently in four ways.

1. Expand the three skeleton phases symbolically and reconstruct their
   three nonempty Dyck components.
2. Re-extract first and last returns from a general output defect, rather
   than assuming that phase change commutes with extraction.
3. Count marked top-level atomic factors by generating functions.
4. Reduce the proposed macroscopic correction to an ordinary graph
   incidence matrix and check connectivity, lattice saturation, and the
   signs of every cut inequality.

No SAT, exhaustive search, or certificate data are used.

## 2. Six-filler block: valid

Root a lower defect as

\[
 0(1u_0 0v_0)0(1u_1 0v_1)0(1u_2 0v_2).                    \tag{2.1}
\]

Writing the three skeleton coordinate classes as `Q_A,Q_B,Q_C`, direct
cyclic reading gives

\[
\begin{array}{c|c|c}
\text{phase}&\text{root class}&\text{three Dyck components}\\ \hline
B&A&1u_i0v_i\\
A&C&v_i10u_{i+1}\\
C&B&u_i1v_i0.
\end{array}                                                  \tag{2.2}
\]

Every component in the last two rows is a concatenation of Dyck words and
contains a displayed `10` or `1v_i0`; it is therefore nonempty Dyck.  This
proves all three lower rows.

For an upper pairwise union, its complement has filler one-set `G`, not
`H`.  Plain complement is not a Dyck operation.  Coordinate reversal sends
`G` to the one-set of the reverse-complements of the six fillers, which are
Dyck, and reverses the skeleton phase.  Hence reverse-complementation, not
plain complementation, proves the upper row.  The theorem states this
explicitly.

Verdict: **valid**.

## 3. Canonical incidence: corrected

The invalid shortcut was:

> each physical defect has three canonical block incidences, so uniform
> block weight `1/3` is a fractional perfect cover.

It fails because the displayed central `10` in (2.2) need not be the first
or last primitive factor chosen by canonical re-extraction.

For a nonempty Dyck word `a`, let `kappa(a)` count its top-level primitive
factors equal to `10`.  For `y=(y_0,y_1,y_2)`:

* the first-return decomposition gives one incidence;
* the last-return decomposition gives one incidence;
* a cross-sector preimage is equivalent to choosing independently one
  top-level atomic `10` in every `y_i`.

Thus

\[
                     \deg(y)=2+\prod_i\kappa(y_i).           \tag{3.1}
\]

An explicit `n=5` witness is obtained by taking `u_0=10` and all other
fillers empty.  One output component is `1010`; its canonical first return
is the first `10`, not the structural central `10`.  This witnesses the
noncommutation literally.

At `n=5`, the two cyclic types are

\[
 P=(1100,10,10),\quad \deg P=2;
 \qquad
 R=(1010,10,10),\quad \deg R=4.                              \tag{3.2}
\]

There are eleven of each, and every canonical labelled block has type
`P+2R`.  Dual weights `-2` on `P` and `+1` on `R` vanish on every canonical
column but have total `-11`.  Hence the canonical family itself has no
fractional perfect cover.

Verdict: the old 3-regular claim is **false**; equations (3.1) and the
operator in the audited theorem are **valid corrections**.

## 4. Zero-sum charge: valid

Marking a top-level atomic factor `10` in a Dyck word gives an arbitrary
Dyck prefix, the factor `10`, and an arbitrary Dyck suffix.  Its generating
function is

\[
                            C(z)zC(z)=zC(z)^2=C(z)-1.         \tag{4.1}
\]

This equals the generating function for a nonempty Dyck word.  Cubing and
using the identical cyclic-label/root quotient proves

\[
                  \sum_y\prod_i\kappa(y_i)=D_n.             \tag{4.2}
\]

Therefore

\[
             b(y)=1-\prod_i\kappa(y_i),qquad \sum_yb(y)=0.  \tag{4.3}
\]

There is also an exact sourcewise identity

\[
                         b=\sum_x(e_x-e_{\tau x}).            \tag{4.4}
\]

because the coefficient at `y` is one minus `|tau^{-1}(y)|`, namely
`1-prod_i kappa(y_i)`.  Thus the first macroscopic flow is explicit: send
one unit along every arc `tau x -> x`.  The connected-state argument below
is a finite local factorization mechanism, not the source of zero-sum
balance.

The canonical all-one scaled ledger has load `3-b`, so weight `1/3` has
defect `b/3`.  Reverse-complement reverses the order of top-level primitive
factors and fixes an atomic `10`; it preserves `kappa`.  Thus the upper
charge is the reflected lower charge.

Verdict: **valid**, including the direct flow (4.4).

## 5. Connectivity: valid, with the physical root quotient included

Within a fixed rooted layer, contextual Tamari rotations connect all Dyck
words of one semilength.  They can normalize a component to `(10)^s`.
Peak transfer can then change every positive three-part composition of
`N` to `(N-2,1,1)`, without emptying a donor.  Hence each rooted layer is
connected.

The physical palette graph is the union of these rooted layers after identifying
the three roots of each defect.  For `n>=5`, layer intersections contain
separator translations by `3` and by `5`: use an intervening component of
semilength one or two, respectively, and split the remaining component mass
positively.  Since `gcd(3,5)=1`, these overlaps connect all root coordinates
modulo `q=2n+1`.  At `n=4`, every component is `10`, so `b=0` and no routing
is required.

Verdict: **valid after explicitly taking the physical root quotient**.  A
claim that each rooted copy separately routes the physical charge would
triple-count states; the theorem does not make that claim.  A literal
occurrence-labelled state which retains one chosen absolute root needs an
additional reroot-slide packet or must be handled in separate rooted
components.

## 6. Integral flow and cuts: valid

On a connected graph, the integer incidence lattice is precisely the
zero-sum integer lattice.  Root a spanning tree and put on each parent edge
the charge sum below it.  This gives an explicit integer flow with
divergence `b`.  This proves abstract count balancing, not literal packet
installation.

For a directed capacitated transporter graph with convention

\[
                     \partial f=\text{inflow}-\text{outflow},             \tag{6.1}
\]

summing over `S` gives

\[
 b(S)=f(\delta^-(S))-f(\delta^+(S)).                         \tag{6.2}
\]

Therefore the necessary cuts are

\[
 b(S)\le c(\delta^-(S)),\qquad -b(S)\le c(\delta^+(S)).      \tag{6.3}
\]

Here the demand is explicitly
`b(S)=|S|-|tau^{-1}(S)|`, by the sourcewise identity (4.4).

The standard supersource/supersink reduction proves sufficiency and
integrality.  If only an uncapped subgraph is available, each component
preserves its charge sum.  The minimum signed-residual `l_1` norm is exactly
the sum of the absolute component charges.

Verdict: **valid under the theorem's serializable-capacity hypothesis**.
Shared packet resources require an expanded capacity/Rado system and are
not covered by scalar edge capacities.

## 7. What is proved constructively

The theorem does more than expose another obstruction.

* It replaces the false four-copy picture by one exact child-layer charge
  vector.
* That charge has zero total in every dimension.
* Two finite contextual move schemas connect the complete abstract state
  bank.
* Their graph incidence matrix is saturated, so the charge always has an
  integral abstract routing.
* Any failure of a certified physical subcatalogue is an explicit Hoffman
  cut or component charge, and a bounded total component charge is exactly
  a finite residual basis.

The first required noncanonical move is already forced at `n=5`:
`1100 <-> 1010`.  Thus a crossed/Tamari packet is the correct constructive
next object.

## 8. Remaining hypothesis and scope

Unproved:

1. a literal paired transporter for the Tamari and sector-transfer schemas;
2. common lower/upper occurrence labels on that transporter;
3. nonnegative/serializable capacity for the spanning flow;
4. preservation of owner, residence, deeper shadows, topology, and the
   common-cap compiler;
5. integral disjoint block rounding after the fractional/ledger balance.

Accordingly the theorem does not prove `B(k)+O(1)`.  It proves the exact
macroscopic defect-count flow and reduces the remaining central palette
gate to two finite packet schemas plus explicit cut inequalities.
