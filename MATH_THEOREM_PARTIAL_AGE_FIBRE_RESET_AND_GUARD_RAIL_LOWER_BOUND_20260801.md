# Partial age-fibre reset and the unavoidable guard rail

Date: 2026-08-01

Status: unconditional fibre/collar characterizations and an unconditional
lower bound on continuously owner-changing synchronizers.  The lower bound
is on protected state resources, not on additive word length.  No
all-dimensional rolling reset is claimed.

## 1. Exact collar action on a partial age fibre

Fix an owner `T` and depth `d`.  An age-labelled state is an ordered
partition

\[
 P=(C_0,\ldots,C_d),\qquad
 T=C_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d.
\]

Write `a_P(x)=i` when `x in C_i`.  Let `F` be any family of such states and
let

\[
                         B_1,\ldots,B_q\subseteq T,
                         \qquad q\le d+1               \tag{1.1}
\]

be a fixed nonempty-letter collar.  Put

\[
 U_t=B_1\cup\cdots\cup B_t,
\]

and, for `x in U_t`, let `ell_t(x)` be its last occurrence among
`B_1,...,B_t`.

### Theorem 1.1 (partial-fibre collar criterion)

The collar is legal from every state `P in F` through time `q` if and only
if, for every `1<=t<=q`,

\[
 \boxed{
   \bigcup_{P\in F}\{x:a_P(x)>d-t\}\subseteq U_t .}   \tag{1.2}
\]

Conditioned on legality, all terminal states are equal if and only if

\[
 \boxed{
   a_P(x)\text{ is independent of }P\in F
   \quad\text{for every }x\notin U_q .}               \tag{1.3}
\]

#### Proof

If `x` has appeared in the collar, its age at time `t` is

\[
                         t-\ell_t(x)\le t-1\le d.
\]

If it has not appeared, its age is `a_P(x)+t`; it remains in the owner
window exactly when this is at most `d`.  Taking the union over `F` gives
(1.2).

At the terminal time, a hit coordinate has the fixed age
`q-ell_q(x)`.  An unhit coordinate has age `a_P(x)+q`, so its final age is
independent of `P` exactly under (1.3).  `square`

This theorem distinguishes two resources which aggregate age types merge:
coordinates whose old age must be known, and coordinates which the collar
actively refreshes.

## 2. Full type fibres

For a composition `c=(c_0,...,c_d)`, let `F_c` contain every ordered
partition of `T` with block sizes `c`.  Put

\[
                         j(c)=\max\{i:c_i>0\}.
\]

### Corollary 2.1

If `c` has at least two positive parts, every synchronizing collar for the
full fibre `F_c` must satisfy

\[
                         U_q=T.                       \tag{2.1}
\]

Moreover every collar legal from all of `F_c` satisfies

\[
                         U_{d-j(c)+1}=T.              \tag{2.2}
\]

Conversely, a fixed collar whose union is already `T` by that time is legal
from the full fibre and has a state independent of the initial partition
once every coordinate has been hit.

#### Proof

If two blocks of `c` are positive, every fixed coordinate can occupy either
of two different ages in members of `F_c`.  Equation (1.3) therefore forces
every coordinate into `U_q`, proving (2.1).

At time `t=d-j(c)+1`, every coordinate can occupy the oldest nonempty block
`C_(j(c))` in some member of the full fibre.  If it has not appeared, its
age becomes `j(c)+t=d+1`, so (1.2) forces (2.2).  The converse is immediate
from Theorem 1.1.  `square`

If `c` has only one positive part, its literal fibre is already a singleton;
no synchronization is required.

## 3. Static reset by nested flags is minimal

For a partition `P`, write

\[
                         S_j=C_0\cup\cdots\cup C_{j-1}
                         \qquad(1\le j\le d).         \tag{3.1}
\]

Delete repetitions caused by zero blocks.

### Theorem 3.1 (minimal full-flag address)

For a fixed owner and type, the owner together with all distinct proper
sets in (3.1) determines the literal partition uniquely.  If one boundary
between two positive consecutive blocks is omitted, the remaining nested
sets do not determine the partition: swapping one element across that
boundary gives two different states with every retained address equal.

Hence a type with `p` positive age blocks requires at least `p-1` nested
boundary addresses for a static unique-fibre reset.  In particular, a
fully positive depth-`d` type requires all `d` addresses.

#### Proof

With every boundary present,

\[
 C_0=S_1,\quad C_i=S_{i+1}-S_i\ (1\le i<d),quad
 C_d=T-S_d,
\]

so the partition is recovered.  If the boundary between two positive
blocks is absent, the two blocks appear only through their union in every
retained prefix.  Exchanging one element from each block preserves their
sizes and every retained prefix, but changes the partition.  `square`

Thus occurrence-labelled lower targets can kill holonomy without adding
positions, but only by supplying the complete nested flag.  Aggregate rank
capacities alone do not choose this flag.

## 4. The physical Johnson guard-rail lower bound

Now allow the owner to change.  Let

\[
 T_0,T_1,\ldots,T_q
\]

be a simple Johnson path, with

\[
 T_t=T_{t-1}-\{\alpha_t\}+\{\beta_t\}.              \tag{4.1}
\]

Assume the literal age update is physical: `alpha_t` is in the oldest class
of the state at `T_(t-1)`, and the fresh `beta_t` enters age zero.  Assume
no `beta_t` was present earlier in the path.

### Theorem 4.1 (departure queue)

For `1<=t<=min(q,d+1)`, the leaving coordinate `alpha_t` belongs in the
initial state to the exact age block

\[
                         \boxed{\alpha_t\in C_{d-t+1}.}              \tag{4.2}
\]

In particular, a prescribed collar which changes owner at each of its first
`d+1` transitions requires a protected ordered deletion queue

\[
                         \alpha_1\in C_d,\alpha_2\in C_{d-1},\ldots,
                         \alpha_{d+1}\in C_0.          \tag{4.3}
\]

No coordinate inserted during those transitions can replace an earlier
member of the queue.

#### Proof

The coordinate inserted at transition `s` has age `t-s-1<d` immediately
before every transition `t<=d+1`, so it cannot yet be the required oldest
coordinate.  Thus `alpha_t` was present initially.  Since it has not left
earlier and is oldest immediately before transition `t`, its initial age
plus `t-1` is `d`, proving (4.2).  Distinct transitions delete distinct
initial coordinates, giving (4.3).  `square`

This is the exact dynamic analogue of Theorem 3.1.  A continuously moving
synchronizer avoids repeated owners only by exporting `Theta(d)` protected
state: one scheduled departure from every age class.  After transition
`d+1`, the first entering coordinate has reached age `d` and the queue may
be regenerated periodically.

## 5. Why this is not an additive-length lower bound

Theorem 4.1 costs `d+1` protected incidences, but all `d+1` transitions may
be genuine distinct rank-`r` owner transitions.  They need not be extra
word positions.  The proved pivot-rich resident geodesic packet supplies
exactly this kind of length-`d+1` rolling coordinate geometry locally:
its active coordinates have runs of length `d+1` and its owners are
distinct Johnson neighbours.

Therefore no `Omega(d)` lower bound on **additional length** follows from
age synchronization once variable deadlines/nonflat carriers are allowed.
The full-letter reset from
`MATH_THEOREM_AGE_TYPE_DELAYED_LIFT_LCM_BOUND_20260801.md` is expensive only
because it empties the departure queue and must stutter until a new oldest
coordinate matures.

At the abstract deadline level the distinction is unavoidable.  A
length-`q` block whose union is one owner can be surrounded by shifted
rank-`r` witness intervals which each omit a different private coordinate;
only the full block witnesses that owner.  The sharp pivot-aperture
construction realizes this locally with distinct rank-`r` Johnson owners.
Hence monotone variable deadlines alone cannot prove that every
synchronizer creates `Omega(d)` duplicate central deadlines.

What **is** proved is the resource lower bound

\[
 \boxed{
   \text{static synchronization uses a complete nested flag, or a
   nonstuttering dynamic synchronizer exports a }\Theta(d)\text{ guard rail.}
 }                                                               \tag{5.1}
\]

## 6. Exact remaining lemma

The smallest credible interface is a **rolling guarded reset**:

1. enter with the ordered queue (4.3);
2. refresh every coordinate whose age is not already fixed;
3. change owner at every transition, so no central owner is duplicated;
4. preserve the immediate and arbitrary-width upper palettes; and
5. leave with the same kind of queue, now headed by the coordinates inserted
   during the collar.

Theorems 1.1 and 4.1 give its exact per-coordinate legality and minimum
state size.  Theorem 3.1 gives the alternative static full-flag interface.
What remains open is a correlated host theorem placing either interface in
one lower-exact owner chronology with a terminal occurrence matching.

