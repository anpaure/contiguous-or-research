# Protected complement exchange: Hall, LLL, nibble, and the all-dimension RSB hypothesis

Date: 2026-07-31  
Lane: A, probabilistic/expansion theorem after the connected `K17` `OPTIMAL28` carrier  
Status: unconditional abstract selection theorems and exact `K17` quantitative
reduction; the required protected balanced-circuit supply is not yet proved
for `K17` or in all dimensions

## 0. Verdict

The exact `K17` counts prove individual **raw edge** supply, but they do not
yet prove simultaneous repair.

* Keeping the old macro/packet skeleton is impossible: even after all
  residual pairings are relaxed, `218` rank-ten targets have no provider.
* Releasing complement interiors removes every audited rank-ten singleton
  support obstruction in the `218`/`1900` families.  The `218` static holes
  have `6419` serving columns and the `1900` holes of the saved cycle have
  `66223`; every hole has between `10` and `45` columns.
* A raw column is not a physical repair.  It normally changes four owner
  degrees, and a simultaneous selection must also preserve one lower colour
  per edge, connectedness, residence, every old upper witness, ranks
  `11--12`, and the two bank interfaces.  The `10--45` figures therefore are
  not list sizes for an LLL.

This note proves the appropriate positive theorem.  First close raw columns
into **balanced Hamilton-safe alternating atoms** and attach exact run,
provider, witness, and cap-guard signatures.  Put two atom copies in conflict
whenever their simultaneous use is not literally certified.  For correlated
obligation packets with candidate-list sizes in `[L,L^+]` and maximum
candidate conflict degree `Delta`, a full simultaneous repair exists if

\[
                         L^2\ge 2eL^+\Delta.          \tag{0.1}
\]

No deficit-independence assumption occurs: every casualty and every
provider withdrawal is already encoded in the candidate signatures and the
conflict graph.

In resource form, if each candidate footprint has size at most `w`, one
resource occurs in at most `lambda` candidates of any one packet list, the
minimum list size is `D`, and the packet-interaction degree is `sigma`, the
checkable sufficient inequality (for `sigma>=1`; `sigma=0` is trivial) is

\[
                         D\ge e w\lambda(2\sigma-1).        \tag{0.1a}
\]

There is also an unconditional nibble/alteration bound.  One compatible
batch repairs at least, when `Delta>0`,

\[
 {1\over2}\min\left\{1,{L^2\over L^+\Delta}\right\}             \tag{0.2}
\]

of the current packets.  A hereditary version of the same supply, followed
by a bounded exact absorber, gives a complete repair.  If `Delta=0`, all
packets are compatible and the repaired fraction is one.

If one formally uses all raw `K17` lists, `L=10,L^+=45` and (0.1) would
require `Delta<0.409`, hence `Delta=0`.  If every list could first be lifted
to closed packets and then truncated to ten, the same theorem would permit
only `Delta<=1`.  Neither substitution is presently legitimate: the
`10--45` objects are unbalanced raw columns, and no closed-packet list or
conflict degree has been measured.  The next exact census is the
balanced-circuit closure and its protected conflict degree, not another
count of raw provider edges.

There are two recursive conclusions.  Zero-defect guarded expansion supplies
only the fixed-dimensional repair clause of exact RSB; a separate
parent-to-child Pascal transition is still required.  For `B(k)+O(1)`, a
uniformly bounded terminal central/palette defect may instead be appended
literally, but every defect exported to the next dimension must still be
reset or contracted.  The bounded-defect target is therefore weaker than
exact CLMT and stronger than a one-time partial nibble.

## 1. Exact carrier and raw exchange columns

Let `C` be the `20202` owners in the complement of the fixed `4108`-owner
marked path.  Let `Gamma` be the `20201` lower colours on the complement
path.  For `c in Gamma`, write

\[
                      e_c^0=\{a_c,b_c\}              \tag{1.1}
\]

for the current edge of colour `c`.  A raw exchange column is

\[
       x=(c;u,v),\qquad u,v\in C,\quad u\cap v=c,     \tag{1.2}
\]

and means delete `a_cb_c` and add `uv`.  Its signed owner boundary is

\[
             \partial x={\bf e}_u+{\bf e}_v
                          -{\bf e}_{a_c}-{\bf e}_{b_c}
                    \in\mathbb Z^C.                  \tag{1.3}
\]

The complete marked-preserving catalogue has `545721` off-source columns.
For the current upper holes it has

```text
hole family                    holes    columns    lower colours    support
fixed-skeleton zero rows         218       6419             5220      10..45
all current rank-ten holes      1900      66223            16471      10..45.
```

For one rank-ten target `H`, every serving column has a distinct lower
colour: its endpoints are the two rank-nine facets of `H` complementary to
the two points of `H setminus c`.  Indeed, if `H setminus c={p,q}`, the
edge is exactly `{H setminus {p},H setminus {q}}`; hence `c` determines the
column.  Across different targets the same lower colour may recur.

### Proposition 1.1 (two unavoidable raw cuts)

Let `X` be a family of rank-ten holes.  If a marked-preserving repair assigns
one newly selected edge to each member of `X`, then

\[
 \left|\Gamma(X)\right|\ge |X|,                      \tag{1.4}
\]

where `Gamma(X)` is the set of lower colours of columns serving at least one
member of `X`.  Moreover, for its entire selected column set `S`,

\[
                         \sum_{x\in S}\partial x=0.  \tag{1.5}
\]

#### Proof

Only one replacement can be selected for one lower colour, proving (1.4).
At every complement owner, final degree must equal old degree.  Summing the
degree changes (1.3) gives (1.5).  \(\square\)

Neither row follows from `10--45` individual support.  The global counts
`5220>218` and `16471>1900` also do not prove the subset inequalities
(1.4), and (1.5) is an independent integral circulation condition.

### Proposition 1.2 (abstract support-count countermodel)

For every `L>=1` there is an abstract raw-list incidence instance in which each of
`L+1` holes has `L` candidate columns but no simultaneous lower-rainbow
selection.

#### Proof

Join every hole to the same set of `L` lower colours, with one column for
each target--colour pair.  Every hole has support `L`, but the whole family
has only `L` colour resources, so (1.4) fails.  Separately, one may give
columns distinct colours but boundary vectors contained in an open pointed
halfspace, so no nonempty selection can sum to zero in (1.5).  \(\square\)

This does not assert a literal Johnson realization.  It proves that row
supports alone cannot imply the required Hall rows; the actual Johnson
catalogue must be tested on all subsets.  Thus individual deficits cannot be
sampled independently.

### Proposition 1.3 (exact integral kernel lift)

Let `E` be the complete set of admissible coloured complement edges.  Form
the zero--one matrix `B` with one row for every complement owner and one row
for every lower colour: the column of `e={u,v}` has ones in the rows `u,v`
and in the row equal to the lower colour of `e`.  If `x^0,x in {0,1}^E`
have the same prescribed owner degrees and select exactly one edge of every
lower colour, then

\[
                         z=x-x^0\in\ker_{\mathbb Z}B.       \tag{1.6}
\]

If `z=0`, take `t=0`.  Otherwise `z` is a conformal sum

\[
                         z=g_1+\cdots+g_t                 \tag{1.7}
\]

of nonzero conformally indecomposable integer kernel vectors.  Every `g_j`
has entries in `{0,+1,-1}`, and every partial selection

\[
                         x^0+\sum_{j\in J}g_j             \tag{1.8}
\]

is again zero--one and has the same owner degrees and lower-colour totals,
for every `J subseteq {1,...,t}`.

#### Proof

The owner rows of `B(x-x^0)` are the degree differences and the colour rows
are the palette-count differences, proving (1.6).  Order integer vectors by
`g sqsubseteq z` when they are sign-compatible coordinatewise and
`|g_e|<=|z_e|` for every `e`.  If `z` is not indecomposable in this order,
write it as two nonzero sign-compatible kernel vectors and repeat.  The
`ell_1` norm strictly decreases at every split, so the process terminates
and gives (1.7).

Since `z_e` belongs to `{0,+1,-1}` and every summand is conformal to `z`,
each `g_j` has the same three-valued property.  A coordinate with `z_e=+1`
starts at `x_e^0=0` and is increased by exactly one selected summand; a
coordinate with `z_e=-1` starts at one and is decreased by exactly one.
Thus every partial sum (1.8) remains zero--one.  Every `g_j` lies in the
integer kernel, so the degree and palette rows remain exact.  \(\square\)

In particular, at every colour changed by one summand, its colour row zero
forces one deleted and one added edge.  Thus each summand is itself a
palette-exact multi-edge packet; its missing certificates are geometric,
not marginal.

Proposition 1.3 is an exact algebraic reason to use multi-edge packets.
It does **not** supply Hamilton connectivity, chronology, residence, or
shadow safety; those are the guards imposed next.

## 2. Balanced guarded alternating atoms

### Definition 2.1 (closed exchange atom)

A **closed exchange atom** `A` is a finite set of raw columns satisfying:

1. its lower colours are distinct;
2. `sum_(x in A) partial x=0`;
3. applying all its edge replacements preserves the frozen marked path and
   its two cross edges and leaves one Hamilton owner cycle; and
4. its exact signed-fragment action and the resulting mixed-rank zipper have
   been materialized.

Equivalently, its old/new symmetric difference is a union of alternating
circuits, with the declared circuit packet chosen so the final factor is one
cycle.  Conditions 1--3 give exact owner degree, lower palette, marked-bank,
and topology preservation.  Condition 4 is what makes residence and upper
shadows meaningful.

For a materialized atom record:

* `supp(A)`: all changed old/new incidences and lower colours;
* `halo(A)`: its run-state and five-row envelope/cap collar;
* `Delta_A(R)`: the exact interval-provider derivative of every required
  target `R` (in particular ranks ten--twelve for the present `K17`
  deficits, and every higher-rank anchor which the atom can touch);
* `rep(A)`: replay-defect tokens removed and created; and
* designated physical provider occurrences for every hole it claims to
  repair.

These are literal signatures, not marginal scores.

### Definition 2.2 (private witness bank)

Choose one physical interval witness for every currently covered required
upper target.  A candidate atom is **old-witness safe** if it leaves that
witness unchanged or supplies a declared replacement witness inside its own
support.  For every hole served by an atom, choose one new provider interval
as its designated witness.  The invalidation footprint of an atom is defined
against the entire catalogue of candidate-exported anchors, not merely the
initially chosen base witnesses.

Two candidate copies conflict if either one changes the other's old or new
designated witness.  They also conflict if they share a lower colour,
owner-incidence resource, seam/run halo, socket ticket, or any preallocated
common-cap guard cell.

This device is deliberately stronger than signed expected load.  An
independent candidate family preserves one literal witness for every old and
new target, so rotating casualties are impossible.

### Definition 2.3 (two-closed guarded bank)

Partition the current obligation set into packets

\[
                         \mathcal O=(O_1,\ldots,O_n). \tag{2.1}
\]

A packet may contain several replay tokens and several holes whose physical
supports interact.  Let `A_i` be a finite list of copies of closed atoms,
each of which removes every obligation in `O_i`, creates no unassigned replay
defect, and carries designated witnesses for its serviced holes.

Let `K` be the conflict graph on the disjoint union of the lists.  The bank
is **two-closed** if every independent partial transversal of `K` (at most
one candidate from each obligation list) is jointly literal:

* its alternating actions commute and retain one owner cycle;
* its run and envelope signatures concatenate without an unrecorded
  higher-order seam effect;
* all protected/provider tickets remain within capacity; and
* the marked path, lower palette, and declared boundary state are unchanged.

Two-closedness is a substantive physical hypothesis.  Pairwise disjoint raw
edges do not imply it; the signed-fragment order and the provider/cap halos
must be included when `K` is built.

### Lemma 2.4 (independent transversal implies simultaneous repair)

If a two-closed guarded bank has an independent transversal

\[
                   A_i\in\mathcal A_i\quad(1\le i\le n),       \tag{2.2}
\]

then the composed exchange preserves the owner set, every lower colour, the
marked path, connected topology, all anchored upper targets, and all declared
residence/boundary guards, while repairing every packet in `O`.

#### Proof

Each selected atom is balanced and lower-colour exact.  Two-closedness makes
their composition a literal Hamilton-safe exchange and makes the run/envelope
signatures exact.  Every obligation belongs to a serviced packet.  Old
witnesses and the designated new witnesses survive because every candidate
which could destroy one is adjacent in `K` to its owner.  \(\square\)

## 3. Three exact expansion criteria

Represent the same physical atom in two lists by two copies and join those
copies in `K`.  Thus an independent transversal never reuses one atom.

Put

\[
 L=\min_i|\mathcal A_i|,qquad
 L^+=\max_i|\mathcal A_i|,qquad
 \Delta=\Delta(K),                                   \tag{3.1}
\]

where conflicts inside one list are omitted because only one member of that
list is selected.

### Theorem 3.1 (orthogonal Hall face)

Suppose there is a subbank `B` of physical atoms such that distinct members
of `B` are mutually compatible.  Join packet `O_i` to the atoms in
`B cap A_i`.  If

\[
                       |N(X)|\ge |X|\qquad(X\subseteq\mathcal O), \tag{3.2}
\]

then a simultaneous repair exists.

#### Proof

Hall's theorem gives distinct representatives, which are mutually
compatible by hypothesis.  Apply Lemma 2.4.  \(\square\)

This is the exact role of Hall: it applies after physical orthogonality, not
to the unclosed raw edge lists.

### Theorem 3.2 (sparse-conflict LLL)

If

\[
                         L^2\ge 2eL^+\Delta,          \tag{3.3}
\]

then the guarded bank has an independent transversal and hence a
simultaneous repair.

#### Proof

Choose one member of every list independently and uniformly.  For every
conflicting pair `a in A_i`, `b in A_j`, let `E_(a,b)` be the event that both
are chosen.  Its probability is at most `L^(-2)`.  It depends only on the
two list variables `i,j`.

The number of conflict events involving one list `i` is at most

\[
                    \sum_{a\in\mathcal A_i}\deg_K(a)
                    \le L^+\Delta.                  \tag{3.4}
\]

Hence one bad event has dependency degree at most
`2L^+ Delta-1`.  The symmetric Lovasz local lemma applies because

\[
 eL^{-2}\bigl((2L^+\Delta-1)+1\bigr)\le1.           \tag{3.5}
\]

Avoiding all bad events gives an independent transversal; Lemma 2.4 gives
the physical conclusion.  \(\square\)

More generally, an asymmetric LLL may use the actual list sizes and actual
event dependency graph.  Equation (3.3) is the clean dimension-uniform
criterion.

### Proposition 3.3 (explicit anchor contribution)

Split candidate conflicts into non-anchor conflicts, of maximum degree
`Delta_0`, and the witness-anchor conflicts of Definition 2.2.  Suppose a
candidate exports at most `a_A` anchor footprints and can destroy at most
`a_D` footprints.  Suppose one footprint is destroyed by at most `kappa_D`
candidates and exported by at most `kappa_A` candidates.  Then

\[
       \Delta\le \Delta_0+a_A\kappa_D+a_D\kappa_A.          \tag{3.6}
\]

#### Proof

At most `a_A kappa_D` candidates can destroy an anchor exported by a fixed
candidate.  At most `a_D kappa_A` candidates can export an anchor which the
fixed candidate destroys.  Add the non-anchor neighbours.  \(\square\)

This is the quantitative cost of preventing rotating casualties.

### Theorem 3.4 (resource-footprint LLL)

Suppose every conflict is represented by intersection of finite resource
footprints `R(A)`.  Assume

\[
 |\mathcal A_i|\ge D,\qquad |R(A)|\le w,
 \qquad
 \max_{i,r}|\{A\in\mathcal A_i:r\in R(A)\}|\le\lambda.      \tag{3.7}
\]

Join two packet indices when some pair of their candidate footprints meet,
and let `sigma` be the maximum degree of this packet-interaction graph.  If
`sigma=0`, every choice is compatible.  If `sigma>=1` and

\[
                       D\ge e w\lambda(2\sigma-1),          \tag{3.8}
\]

then the guarded bank has an independent transversal.

#### Proof

Choose one candidate uniformly from every list.  For an interacting pair
`i,j`, let `B_ij` say that the two chosen footprints meet.  The number of
conflicting candidate pairs is at most

\[
 \sum_{A\in\mathcal A_i}\sum_{r\in R(A)}
       |\{A'\in\mathcal A_j:r\in R(A')\}|
 \le |\mathcal A_i|w\lambda.
\]

Consequently `Pr(B_ij)<=w lambda/D`.  The event uses only variables `i,j`
and depends on at most `2sigma-2` other such events.  The symmetric local
lemma applies under (3.8).  Avoiding every `B_ij` gives an independent
transversal, so Lemma 2.4 applies.  \(\square\)

Resources may be lower colours, owner incidences, run collars, old or new
provider occurrences, topology tickets, or compiler cells.  The theorem is
valid only when this list encodes every conflict.

### Theorem 3.5 (nibble by random activation and alteration)

If `Delta>0`, put

\[
 \theta=\min\left\{1,{L^2\over L^+\Delta}\right\},\qquad
 \beta={\theta\over2}.                               \tag{3.9}
\]

There is a compatible partial transversal servicing at least `beta n`
packets.  If `Delta=0`, all `n` packets can be serviced.

#### Proof

Activate every packet independently with probability `theta`; for each
active packet choose a uniform candidate.  There are at most

\[
                {1\over2}nL^+\Delta                 \tag{3.10}
\]

conflicting candidate pairs.  A fixed pair is selected with probability at
most `theta^2/L^2`.  If `A` is the number of active packets and `C` the
number of selected conflict edges, then

\[
 \mathbb E(A-C)\ge
 n\left(\theta-{L^+\Delta\theta^2\over2L^2}\right)
 \ge {\theta n\over2}.                              \tag{3.11}
\]

From any outcome delete at most one chosen endpoint for each conflict edge.
At least `A-C` choices remain and they are independent.  Some outcome
therefore retains at least `beta n` choices.  \(\square\)

### Theorem 3.6 (resource-footprint nibble)

Under (3.7), put

\[
 \xi={\sigma w\lambda\over D},\qquad
 \theta=\begin{cases}
 1,&\xi=0,\\
 \min\{1,(2\xi)^{-1}\},&\xi>0.
 \end{cases}                                             \tag{3.12}
\]

There is a compatible partial transversal servicing at least
`theta n/2` packets.

#### Proof

Activate every packet with probability `theta` and choose a uniform
candidate on every active packet.  Conditional on a fixed chosen candidate,
one active neighbouring packet conflicts with probability at most
`theta w lambda/D`.  A union bound over at most `sigma` neighbours gives
failure probability at most `theta xi`.  Thus a packet is retained with
probability at least

\[
                    \theta(1-\theta\xi)\ge\theta/2.
\]

Delete every chosen candidate which has a conflict.  The survivors are
compatible, and their expected number is at least `theta n/2`; hence some
outcome has at least that many.  \(\square\)

### Corollary 3.7 (hereditary nibble plus absorption)

Suppose that after every compatible batch the residual state is rebuilt with
all old and newly created witnesses protected, and the same lower bound
`beta>0` holds whenever more than `q` packets remain.  Suppose also that
every guarded residual instance of at most `q` packets has an exact absorber
which avoids every resource and anchor frozen in earlier rounds.
Then a complete simultaneous repair exists.

#### Proof

Repeatedly apply Theorem 3.5 or 3.6.  The number of unresolved packets decreases by
at least the factor `1-beta` until it is at most `q`.  Because every batch is
guarded, no repaired packet or old target reappears.  Apply the absorber to
the final residual instance.  \(\square\)

This is a genuine nibble statement, but regeneration is essential.  A
one-time average conflict bound cannot prevent later witness depletion.

### Cost/cap addendum

If every packet `O_i` is allocated a private short-cell/cap budget `s_i`,
every candidate in `A_i` costs at most `s_i`, and

\[
                            \sum_i s_i\le s,          \tag{3.13}
\]

then the selection respects total reserve `s`.  This is only a resource
bound.  A common compiler additionally requires either a named feasible
common-cap core which survives every selected partial transversal, or
packetwise compatible augmenting linkages in the exact common-cap system,
including all unary, pair, and triple obstruction rows.  Entering cap cells
as conflict resources prevents overuse but does not by itself prove such a
common matching.  A scalar reserve alone has no implication.

## 4. What the exact `K17` counts do and do not prove

The fixed-skeleton no-go is decisive for its scope: its `218` zero rows have
empty lists before complement interiors are released.  Hence a residual
`U`-pairing LLL has probability zero of success.

The complete interior exchange atlas makes the raw lists nonempty, but it
has not yet emitted the lists `A_i` of Definition 2.3.  For each service
column one must still find a balanced closure satisfying (1.5), retain one
cycle, materialize its zipper, and filter it through residence and private
upper witnesses.  The minimum protected balanced-list size could in
principle be zero even though the raw size is at least ten.

If one nevertheless inserts all raw lists into the symmetric LLL, then

\[
 {L^2\over2eL^+}={100\over90e}<0.409.                \tag{4.1}
\]

Thus (3.3) would require integer conflict degree `Delta=0`.  The theorem
permits discarding candidates: truncating every list to ten would instead
give `L=L^+=10` and permit only `Delta<=1`.  Neither calculation is an
application to the carrier, because the objects have not been closed into
balanced atoms.  Shared lower colours, owner-balance closure, witness
footprints, and seam halos all remain unmeasured.

There are also macroscopic lower bounds inside the present
marked-preserving, lower-q1-exact standard owner-chronology exchange model.
The current `1900` absent rank-ten labels force at least `1900` new and
`1900` deleted lower-colour edges.  Independently, the strict
complement-run intervals have transversal number `1603`.  The services may
overlap, but every repair in this exchange face is necessarily a large
correlated rethread, not a bounded collar patch.  A genuinely nonflat
compiler lies outside this floor and is not ruled out.

The next proof-safe `K17` computation is therefore:

1. choose a service column and enumerate its degree-balanced alternating
   circuit closures;
2. retain only Hamilton-safe closures and emit their exact `R_3`, `U_12`,
   higher-rank anchor, private-witness, endpoint, and cap-halo signatures;
3. packet the `2392` strict run tokens and the hole vector
   `(1900,911,128)` by overlapping physical support;
4. compute `L,L^+,Delta` and the colour-Hall cuts (1.4); and
5. apply Theorem 3.1, 3.2, 3.4, or the hereditary form of Corollary 3.7.

Optimizing the three deficit families separately would not certify any row
of this procedure.

## 5. Exact and bounded-defect all-dimension hypotheses

The fixed ranks `10--12` are replaced below by the complete target tower
required at the current RSB deadline.  Exact equality and an additive
constant require different terminal clauses.

### Hypothesis `GEX_0(m)` (zero-defect guarded exchange expansion)

Every declared regenerative two-bank prestate in dimension `m` admits:

1. **Correlated packets.**  A packet partition of all replay/residence
   defects, all missing required shadow targets, and all boundary/socket
   debts.  Packets may contain obligations at different depths.
2. **Literal anchors.**  One protected physical witness for every already
   covered required target, and a designated private witness for every
   serviced missing target.
3. **Closed atoms.**  Lists of balanced Hamilton-safe alternating atoms
   preserving the owner deck, complete lower palette, marked bank, required
   voltage/socket state, and the exported RSB boundary state.
4. **Exact composability.**  A two-closed conflict graph containing every
   colour, incidence, run-halo, witness, socket, and cap interaction.
5. **Expansion.**  Either the one-shot inequality

   \[
                    L_m^2\ge2eL_m^+\Delta_m,          \tag{5.1}
   \]

   or, when `Delta_m>0`, hereditary nibble supply with parameter

   \[
      \beta_m={1\over2}\min\left\{1,
                 {L_m^2\over L_m^+\Delta_m}\right\} \tag{5.2}
   \]

   (with `beta_m=1` when `Delta_m=0`) and an exact absorber, disjoint from
   every previously frozen resource, for the terminal residual bank.
   Alternatively one may verify the resource form

   \[
       D_m\ge e w_m\lambda_m(2\sigma_m-1)             \tag{5.2a}
   \]

   or its hereditary footprint-nibble version.
6. **Exact compiler guard.**  Either a named feasible full common-cap
   matching survives every independent partial transversal, or a named
   feasible base matching/core is given and the packets carry mutually
   compatible vertex-disjoint augmenting linkages which, after all selected
   augmentations, yield a full integral common-cap matching.  The exact
   system includes its unary, pair, and triple obstruction rows.  Mere scalar
   slack, those low-order rows alone, or nonoverlap of cap cells is not
   enough.

In a one-shot application, all atoms, anchors, conflicts, and compiler
certificates are finite literal objects emitted before selection.  In the
hereditary version the corresponding bank must be emitted and certified at
every rebuilt residual state before that round's selection (equivalently by
a finite guarded decision tree).  Thus the hypothesis is checkable and is
strictly stronger than raw provider abundance.

### Theorem 5.1 (`GEX_0(m)` supplies the fixed-dimensional repair clause)

If `GEX_0(m)` holds, every declared prestate in dimension `m` has a literal
terminal chronology which preserves the marked bank and lower palette, has
no declared residence/replay defect, covers the full required shadow tower,
retains the exported socket/voltage state, and has one integral common-cap
compiler.

#### Proof

Under (5.1), apply Theorem 3.2; under (5.2), apply Corollary 3.7; under
(5.2a), apply Theorem 3.4, or Theorem 3.6 followed by Corollary 3.7 in its
hereditary form.  Lemma 2.4 gives one literal owner/lower-palette chronology
and preserves all anchors and boundary states.  Every obligation packet is
serviced, and clause 6 gives one common compiler on that same chronology.
\(\square\)

This is only a fixed-dimensional repair theorem.  To iterate it, one still
needs an independently proved parent-to-child Pascal transition which maps
every accepted exported state in dimension `m` to a declared
`GEX_0(m+1)` prestate, together with base states.  Under those additional
hypotheses, Theorem 5.1 supplies the repair clause of exact RSB.  `GEX_0`
alone is not a dimension-changing theorem.

### Hypothesis `GEX_C(m)` (bounded terminal defect)

For an additive-constant theorem, replace exact terminal service by the
following weaker clause.  The selected chronology may leave a terminal
family `H_m` of uniformly bounded repair complexity, including boundedly
many missing middle owners/masks or lower-palette masks.  Here `R(H)` is the
minimum length of a nonempty set-valued word whose interval unions cover
every target in `H`, with `R(emptyset)=0`; literal listing gives
`R(H)<=|H|`.  Let `k=k(m)` denote the physical dimension of the terminal
map (with separate odd/even maps when needed).  Require:

1. the resulting physical word is literal and has length `B(k)+c_m`;
2. `c_m+R(H_m)` is uniformly bounded (or bounded by a declared carried
   potential as below);
3. `H_m` is paid only in this terminal word; and
4. every central, palette, residence, provider, socket, or compiler defect
   needed by the next Pascal transition belongs instead to the exported
   sidecar and is reset or contracted there.

Unlike clause 3 of `GEX_0`, the terminal owner/palette state in `GEX_C` may
therefore be near-exact: the exact kernel acts on its nonexceptional core,
and the bounded residual mismatch is recorded in `H_m` if it is terminal or
in `Phi_m` if it is exported.  Within the present CLMT/RSB route, an exact
ordered four-transversal is required for equality, while a bounded-defect
ordered four-transversal/owner state is enough at a terminal `B+O(1)`
physicalization.  No claim is made that every conceivable equality proof
must use CLMT.  Appending missing masks does not repair the exported sidecar.

### Theorem 5.2 (bounded-defect spine implication)

Assume a separate parent-to-child transition produces an infinite sequence
of declared `GEX_C` prestates with carried potential `Phi_j>=0`, and assume

\[
 \Phi_{j+1}\le\rho\Phi_j+\beta\quad(0\le\rho<1),
 \qquad c_j+R(H_j)\le a\Phi_j+b.                    \tag{5.3}
\]

If every nonterminal obligation is repaired by the guarded exchange theorem
and the required base states exist, then

\[
 \nu(k)\le B(k)+
 \left\lceil a\max\left\{\Phi_0,{\beta\over1-\rho}\right\}+b\right\rceil
                                                               \tag{5.4}
\]

along that spine (with the maximum of the odd/even constants when their
terminal maps differ).

#### Proof

Induction in (5.3) gives
`Phi_j<=max{Phi_0,beta/(1-rho)}`.  The fixed-dimensional guarded theorem
produces the stated physicalization, possibly with the terminal family
`H_j`.  Append a shortest word covering `H_j`.  Terminal repair preserves
all old witnesses and costs `R(H_j)`, giving (5.4).  The appended letters
are not exported; the separately contracted sidecar supplies the next
prestate.  \(\square\)

For an exact one-shot repair it is enough that `L_m^+/L_m=O(1)` and
`L_m/Delta_m -> infinity`, or that
`D_m/(w_m lambda_m sigma_m) -> infinity`, together with all literal guards.
For `B+O(1)`,
a nibble which merely leaves `O(1)` unresolved packets is useful only when
their total terminal repair complexity is bounded and every carried defect
still satisfies the reset/contraction clause.  Probability is used only to
select authenticated physical atoms; it never makes rankwise deficits
independent.

## 6. Adversarial audit and exact boundary

The strongest assertion in this note is conditional on closed balanced
atoms and two-closed conflicts.  This cannot be weakened to raw columns:

* equation (1.5) can fail although every hole has many columns;
* a compatible degree-balanced selection can split the owner cycle;
* a new provider can later be destroyed unless its occurrence is private;
* disjoint changed edges can have interacting long prefix/suffix provider
  states; and
* positive scalar cap slack does not imply a common compiler.

Nor is the fixed-dimensional selection theorem a Pascal transition.  Exact
RSB needs a separately proved exported-state map.  In the additive-constant
variant, terminal middle/palette holes may be appended, but exported
central, residence, provider, or compiler debt may not be discarded.

The LLL proof uses genuine independence only between the per-packet random
choices.  All physical correlations are placed in bad events before the
lemma is invoked.  The nibble theorem likewise deletes actual conflict
edges and assumes hereditary regeneration before iteration.

Unconditional conclusions for the authenticated `K17` carrier are limited
to:

1. the fixed-skeleton residual-pairing lane is impossible;
2. every static and current rank-ten hole has raw marked-preserving interior
   support `10--45`;
3. every repair in the marked-preserving, lower-q1-exact complement-exchange
   face must satisfy colour Hall (1.4), degree circulation (1.5), and the
   exact signed guard rows; and
4. the raw counts do not verify Hall, LLL, nibble regeneration,
   `GEX_0`, or `GEX_C`.

No repaired `K17` chronology, common cap, word, exact all-dimension RSB
theorem, or additive-constant spine is claimed.

The minimal missing positive lemma on this lane is therefore:

> **Protected kernel expansion for the OPTIMAL28 complement.**  Partition
> the correlated residence/replay and rank-ten--twelve obligations, and for
> every packet exhibit a nonempty list of Hamilton-safe integer-kernel atoms
> with complete signed provider and compiler signatures, such that either
> all private-bank Hall cuts hold, (3.3) or (3.8) holds, or the hereditary
> nibble hypotheses plus an exact guarded absorber hold.

The raw `10--45` census does not prove even nonemptiness of these filtered
lists.  Conversely, any one of the stated expansion alternatives would
compose immediately by the theorems above; no further probabilistic lemma is
missing.

## 7. Frozen inputs

The exact finite input and its scope are frozen in:

```text
MATH_THEOREM_AD_K17_OPT28_MARKED_PRESERVING_EXCHANGE_AND_STATIC_SHADOW_GATE_20260731.md
MATH_AUDIT_AD_K17_OPT28_FIXED_SKELETON_STATIC_PROVIDER_NOGO_20260731.md
MATH_THEOREM_AD_K17_MARKED_PATH_COMPLEMENT_RETHREAD_MASTER_20260731.md
MATH_THEOREM_K17_TWO_BANK_SWITCH_MONOIDS_AND_GUARDED_REPAIR_HALL_20260731.md
MATH_THEOREM_K17_OPT28_COMPLEMENT_REPAIR_EDGE_FLOORS_AND_CAP_REBASE_20260731.md
MATH_THEOREM_A_K17_COMPLEMENT_CIRCUIT_CLOSURE_ANCHORED_LLL_20260731.md
SHA-256 eb3187b395b419118a54e6cfc388143f39992873e48c03d82fb70b8f777470ca

MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md
SHA-256 0b069898885e643f21dfb3f9481110dfd9a177a2d11aa34eccc445faa675e11c

scratch/ad_k17_opt28_complement_rethread_master_20260731.audit.json
SHA-256 36fe45cb80f9ae5565885640faa9f4c984001e6503777242a9c273abdbe534b7
payload 4c551b0e6da95c691e38bb40df4f01441e6dc570f6f7f317c484358aa743dde7

scratch/ad_k17_opt28_static_shadow_provider_master_20260731.audit.json
SHA-256 cb10e939bcdb1e73f08f0cca0b6318c52487acd283a49c63be821c9488d2f857
payload e4b23438a5bb315323fdd72567f14819029986777ff3833dac6b0206b96d5593
```
