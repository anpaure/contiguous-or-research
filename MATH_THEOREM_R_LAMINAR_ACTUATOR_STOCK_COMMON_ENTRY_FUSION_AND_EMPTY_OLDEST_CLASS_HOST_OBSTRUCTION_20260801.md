# Laminar actuator stock, common-entry fusion, and the empty-oldest-class host obstruction

Date: 2026-08-01

Status: unconditional age-type stock and fusion theorems, including the
new arbitrary-hole parity-sweep packet, together with an unconditional
obstruction to the literal consecutive-owner lift of the older zero-fill
single-hole actuator.  The positive fusion theorem removes component
proliferation at the age-type level.  It does **not** embed the resulting
type cycle in a protected Catalan/common-cap chronology.

## 0. Verdict

The uniform single-hole and double-hole actuators of handoff items 2496TG,
2498MR and 2500DH use only `3d-1` age types in total.  For arbitrary
multiplicities their reservoir demand is one nested, nonincreasing stock
vector.  Moreover, all actuator copies can be fused into one directed
age-type cycle by transparent two-edge switches at their common entry
types.  Hence neither the number of reservoir *types* nor quotient
component count is the missing theorem.

There is, however, a sharp physical obstruction.  Every standard
single-hole actuator contains its zero-fill donor type `B_j`, whose oldest
age class is empty.  In a flat one-copy chronology, every internal
rank-`r` owner window must have nonempty oldest class.  Consequently each
contiguous owner block contains at most one `B_j`, at its right endpoint.
If `U` single-hole repairs are expanded literally, they require at least
`U` owner blocks and therefore at least `U-1` extra separator windows
(nonmiddle or repeated-owner).  At the first
systematic failure `k=54`, `U=54`; this is a 53-separator calibration, not
by itself an asymptotic lower bound.

Thus the older single-hole quotient actuator cannot be stocked in one
protected Catalan chronology without a linearly accumulating literal
sidecar.  The subsequently proved arbitrary-hole parity-sweep actuator
supplies exactly the required positive-terminal replacement; Section 6A
shows that all of its copies also fuse into one quotient cycle.  Its
owner-labelled, guarded, lower-rainbow partition lift remains open.

## 1. The universal actuator inventory

Fix

```text
d>=3,  r>=d+4,  L=r-d-1.
```

For `2<=j<=d`, let

```text
C_j=(1,L,1,...,1), with coordinate j raised to 2,
D  =(L+1,1,...,1),
Y  =(L-1,1,3,1,...,1),
R_p=(L,1,...,1), with coordinate p raised to 2
     (1<=p<=d-1).
```

Let `B_j` be the zero-fill donor type in the single-hole theorem: its fresh
class is `L+1`, its age-`j-1` class is two, and its terminal age class is
zero.  The already proved directed cycles are

```text
S_j: C_j -> D -> R_1 -> ... -> R_(j-2) -> B_j -> C_j,

T_j: C_j -> Y -> R_1 -> ... -> R_(j-1) -> C_j.       (1.1)
```

For `j=2`, the `R` string in `S_j` is empty.  Cycle `S_j` is the
single-hole completion actuator; `T_j` is the post-regrouping double-hole
actuator.  Both have length `j+1`.

### Proposition 1.1 (linear type inventory)

The union of all types in (1.1), over `2<=j<=d`, has size at most

```text
                         3d-1.                        (1.2)
```

More precisely, it is contained in

```text
{C_j:2<=j<=d} union {B_j:2<=j<=d}
 union {R_p:1<=p<=d-1} union {D,Y}.                  (1.3)
```

#### Proof

The four displayed families have respective sizes `d-1,d-1,d-1,2`.
Every vertex of every cycle in (1.1) belongs to one of them.  This proves
(1.2).  No assertion that all listed types are distinct is needed.  \(\square\)

## 2. Exact laminar stock law

Let `u_j` be the number of single-hole units of position `j`, and let `v_j`
be the number of double-hole units of position `j`.  These are arbitrary
nonnegative integers.  Put

```text
U=sum_(j=2)^d u_j,       V=sum_(j=2)^d v_j,

b_p=sum_(j=p+2)^d u_j + sum_(j=p+1)^d v_j
                                      (1<=p<=d-1).    (2.1)
```

Empty sums are zero.

### Theorem 2.1 (necessary and sufficient standard-cycle stock)

The disjoint union of the requested standard cycles has the exact
post-operation type ledger

```text
n(C_j)=u_j+v_j,              n(B_j)=u_j,
n(D)=U,                      n(Y)=V,
n(R_p)=b_p.                                      (2.2)
```

In particular,

```text
b_1>=b_2>=...>=b_(d-1)>=0,                        (2.3)

sum_(p=1)^(d-1)b_p
   =sum_(j=2)^d (j-2)u_j + sum_(j=2)^d (j-1)v_j.  (2.4)
```

Conversely, copies of the types in (2.2), with the named directed edges in
(1.1), decompose into precisely the requested standard actuator cycles.
Thus (2.2) is necessary and sufficient within this actuator catalogue.

#### Proof

One `S_j` uses `C_j,D,B_j` once and uses `R_p` exactly for
`1<=p<=j-2`.  One `T_j` uses `C_j,Y` once and uses `R_p` exactly for
`1<=p<=j-1`.  Summing gives (2.1)--(2.2).  Formula (2.3) is immediate from
the nested index ranges.  Interchanging the two sums gives

```text
sum_p sum_(j>=p+2)u_j=sum_j(j-2)u_j,
sum_p sum_(j>=p+1)v_j=sum_j(j-1)v_j,
```

which is (2.4).  For the converse, label the copies contributing to each
summand in (2.1) by their `j` and actuator shore.  The named edges of
(1.1) then recover the cycles copy by copy.  \(\square\)

The theorem is a bounded-*type* statement, not a bounded-occurrence
statement.  The total reservoir occurrence mass in (2.4) can be
`Theta(d(U+V))`; no type-count argument can erase that capacity.

## 3. One quotient cycle, not `O(d)` actuator components

The common entry is stronger than the stock count suggests.

### Lemma 3.1 (complete entry adjacency)

For every `2<=j<=d`, both transitions

```text
                         C_j -> D,
                         C_j -> Y                              (3.1)
```

are legal age transitions.

#### Proof

For `C_j->D`, every positive-age coordinate of `D` is one, and every
corresponding prefix coordinate of `C_j` is at least one.  For `C_j->Y`,
the only nonunit requirement is

```text
                         Y_2=3<=C_(j,1)=L,
```

which holds because `L>=3`.  All other shifted inequalities are one
against at least one.  \(\square\)

### Lemma 3.2 (directed two-edge cycle merge)

Let two vertex-disjoint directed cycles contain edges `a->b` and `c->e`.
If `a->e` and `c->b` are also legal, replacing the first two edges by the
crossed pair merges the two cycles into one directed cycle and preserves
the indegree and outdegree of every vertex.

#### Proof

Deleting one edge opens each cycle into a directed path, one from `b` to
`a` and one from `e` to `c`.  The crossed edges concatenate the two paths
in one cyclic order.  The four endpoint degrees are restored exactly.
\(\square\)

### Theorem 3.3 (common-entry fusion)

Every nonempty disjoint union of standard cycles (1.1), with arbitrary
multiplicities `u_j,v_j`, can be changed by legal two-edge switches into
one directed age-type-occurrence cycle.  The switch changes no type count
and no marked-profile marginal.

#### Proof

Distinguish repeated occurrences of the same type.  Each actuator cycle
has one distinguished first edge `C_j->D` or `C_j->Y`.  Take distinguished
edges from any two current cycle components.  By Lemma 3.1 both crossed
edges are legal, regardless of the two values of `j` and regardless of
whether the two heads have type `D` or `Y`.  Lemma 3.2 merges the two
components.  Repeating gives one cycle.

Only adjacency is changed.  Every type occurrence, and hence every marked
payload attached to that occurrence, is retained.  Therefore all marked
rank totals remain unchanged.  \(\square\)

This removes quotient monodromy at the type-occurrence level.  It does not
say that the crossed edges exist between the chosen *literal partition
states*, owner addresses, or common-cap occurrences.  A physical version
would first need a source/state-compatible `2x2` entry rectangle, followed
by a separate lower-colour transport.

There is an additional exact warning: such a rectangle cannot preserve a
strict lower rainbow by itself.

### Lemma 3.4 (no nondegenerate lower-palette-transparent Johnson `C4`)

Let `A,C` be distinct rank-`r` tail owners and `B,D` distinct rank-`r`
head owners.  Suppose all four pairs

```text
A-B, C-D, A-D, C-B
```

are Johnson edges.  If the two perfect matchings have the same multiset of
rank-`r-1` intersection colours,

```text
{A intersect B,C intersect D}
  ={A intersect D,C intersect B},                    (3.2)
```

then all four intersection colours are equal.  Consequently no two-edge
`C4` switch between two edges of a lower-rainbow factor preserves the lower
palette.

#### Proof

There are two ways to match the two members of the multisets in (3.2).
In the first,

```text
A intersect B=A intersect D=:K_A,
C intersect B=C intersect D=:K_C.
```

Both distinct rank-`r` sets `B,D` contain the two rank-`r-1` sets
`K_A,K_C`.  If the latter were distinct, their union would have size at
least `r`; containment in both `B` and `D` would force
`B=D=K_A union K_C`, a contradiction.  Hence `K_A=K_C`, and all four
colours agree.

In the second matching,

```text
A intersect B=C intersect B=:K_B,
A intersect D=C intersect D=:K_D.
```

The same argument inside the distinct sets `A,C` gives `K_B=K_D`, again
making all four colours equal.  A lower-rainbow factor cannot contain the
two original equal-colour edges.  \(\square\)

Thus Theorem 3.3's quotient fusion requires a colour-carrying `C6` or
longer packet (or a simultaneous global lower-palette reassignment) in any
literal lower-rainbow host.  An ordinary Johnson `C4` is not the missing
protected switch.

## 4. The exact physical departure law

Let

```text
A_0,A_1,...,A_d
```

be a literal trace with rank-`r` owner

```text
T=A_0 union ... union A_d.
```

Let `C_i` be its most-recent-occurrence age classes.  Shift once and append
`A_(d+1)`, obtaining owner

```text
T'=A_1 union ... union A_(d+1).
```

### Lemma 4.1 (oldest-class departure)

Always

```text
                         T-T' subseteq C_d.            (4.1)
```

If `|T|=|T'|=r` and `C_d` is empty, then `T'=T`.  In particular, if `T`
and `T'` are distinct Johnson-adjacent rank-`r` owners, then `C_d` is
nonempty and their unique deleted coordinate belongs to `C_d`.

#### Proof

Every coordinate outside `C_d` has a most recent occurrence in one of
`A_1,...,A_d`; it therefore remains in `T'`.  This proves (4.1).  If
`C_d` is empty, then `T subseteq T'`; equal cardinality gives equality.
The Johnson assertion follows.  \(\square\)

The converse local update is also exact.  If `T'=T-{alpha}+{beta}` with
`alpha in C_d`, and `c->c'` is a legal type edge, choose survivor sets

```text
S_i subseteq C_i,  |S_i|=c'_(i+1)       (0<=i<d)
```

and put

```text
C'_0=(C_d-{alpha}) union {beta}
      union union_(i=0)^(d-1)(C_i-S_i),
C'_(i+1)=S_i.                                      (4.2)
```

Then (4.2) has type `c'` and owner `T'`.  Thus nonempty oldest class is the
exact extra condition separating a changing-owner lift from the fixed-owner
age quotient.

### Corollary 4.2 (empty-oldest-class endpoint bound)

Consider a linear word in which a contiguous block of full windows has
pairwise distinct rank-`r` owners.  At most one trace in the block has
`c_d=0`, and if it exists it is the last trace of the block.

For a cyclic one-copy owner chronology, no trace has `c_d=0`.

#### Proof

Every trace except the last is followed by a distinct rank-`r` owner, so
Lemma 4.1 gives `c_d>0`.  In the cyclic case every trace has such a
successor.  \(\square\)

## 5. Sharp empty-oldest-class obstruction to stocking the current single-hole actuator

By construction,

```text
                         (B_j)_d=0.                   (5.1)
```

This is not an optional choice inside the standard single-hole cycle: the
cycle uses the retained zero-fill donor `B_j` as the predecessor of `C_j`.

### Theorem 5.1 (literal block lower bound)

Suppose `U=sum_j u_j` copies of the standard single-hole actuator are
realized literally in a flat rank-`r` one-copy chronology, retaining their
`B_j` occurrences.  If the rank-`r` owner windows are divided into `p`
contiguous one-copy blocks, then

```text
                              p>=U.                   (5.2)
```

Consequently a single final chronology needs at least `U-1` inter-block
separator windows outside its one-copy owner list (each is nonmiddle or a
repeated owner), unless at least `U-1` of the `B_j` occurrences are changed
or removed by a further actuator.

#### Proof

There are `U` distinct retained `B_j` occurrences, each with terminal age
zero.  Corollary 4.2 permits at most one in each flat one-copy block,
proving (5.2).  Joining `p` blocks into one order requires at least `p-1`
intervening full windows outside the one-copy distinct-owner list;
otherwise the adjacent blocks would be one block.  \(\square\)

At `k=54` the first systematic repair moves 54 donor completions and hence
has `U=54`.  The present literal actuator therefore needs at least 53 such
separator windows.  More generally the exact lower bound is `U-1`; it
excludes a dimension-uniform additive constant only along a family for
which `U=U(k)` is unbounded (in particular under the anticipated
`U=Theta(k)` extreme-block hypothesis).  The single finite value 53 does
not itself refute an unspecified absolute constant.

The obstruction is stronger than the earlier fixed-owner warning.  The
age quotient realizes every edge by keeping the owner fixed, which already
repeats the owner.  Lemma 4.1 shows that even allowing a changing Johnson
owner cannot repair the `B_j->C_j` edge: departure from `B_j` is impossible
in the flat one-copy layer.

## 6. What survives for the double-hole bank

Every type in `T_j` has positive terminal age:

```text
(C_j)_d in {1,2},       Y_d=1,
(R_p)_d=1  (p<=j-1<=d-1).                         (6.1)
```

Hence the double-hole family passes Lemma 4.1's necessary owner-change
test.  Theorems 2.1 and 3.3 then prove, unconditionally, that:

1. all double-hole positions use exactly the displayed `2d-1` type slots
   (`C_j`, `R_p`, and `Y`);
2. their reservoir demand is the nested vector

   ```text
   b_p=sum_(j=p+1)^d v_j;
   ```

3. every copy can be fused into one legal age-type-occurrence cycle.

What remains is exactly the occurrence-labelled protected lift.  A
proof-sufficient host state consists of:

1. an owner-simple cyclic or rooted Catalan chronology with one candidate
   occurrence for every vertex of the fused type word;
2. a compatible age-partition path, including the oldest deleted label at
   every transition;
3. literal distinct lower/upper and common-cap payload tickets;
4. a lower-palette-carrying `C6` or longer entry packet implementing the
   switches of Theorem 3.3 (Lemma 3.4 rules out an isolated transparent
   `C4`); and
5. one connected protected-switch graph, so the entry rectangles can be
   applied along a spanning tree without changing residence or the guarded
   payload.

These are joint hypotheses.  Biregularity of the same-owner age-partition
relation supplies none of items 1, 3, or 4.

## 6A. Rebase on the arbitrary-hole parity-sweep actuator

The later theorem
`MATH_THEOREM_R_ARBITRARY_HOLE_PARITY_SWEEP_MARK_ACTUATOR_20260801.md`
replaces the old single-hole completion packet by one uniform
positive-terminal packet for every normalized hole set.  For one repaired
row its occurrence roles lie in

```text
{D,X_m} union {R_1,...,R_d}
  union {Y_(a,u_a):a in L-{m}},                       (6A.1)
```

They use at most `2d+1` distinct age types and at most `3d+3` role
occurrences, and decompose into one base cycle and at most two parity-sweep
cycles.  Every displayed type has positive oldest age:

```text
D_d=1,
(R_p)_d in {1,2},
(Y_(a,u))_d in {1,2},
(X_m)_d>=1.                                          (6A.2)
```

Thus Lemma 4.1's owner-departure obstruction is completely removed for
this replacement packet.

### Theorem 6A.1 (common-`D` fusion for arbitrary holes)

Take any finite multiset of arbitrary-hole parity-sweep packets, allowing
different hole sets and arbitrary multiplicities.  Regard every repeated
type role as a distinct occurrence.  The disjoint union of all constituent
base/parity cycles can be changed by legal two-edge switches into one
directed age-type-occurrence cycle, without changing any occurrence or
marked-rank marginal.

#### Proof

Every constituent cycle contains a distinguished occurrence of type `D`.
Choose its outgoing edge `D_a->h_a`.  For two different cycle components,
choose `D_a->h_a` and `D_b->h_b`.  Since the two tails have the same type,
both crossed edges

```text
D_a->h_b,          D_b->h_a
```

have exactly the same legal type signatures as the original edges.
Lemma 3.2 merges the components.  Iterate along a spanning tree of the
component set.  Only adjacency changes, so every marked payload attached
to a retained occurrence is unchanged.  \(\square\)

For `q` identical repaired rows, this theorem uses the same at most
`2d+1`-type library and `q(3d+3)` or fewer occurrence roles, but exports
only one quotient cycle.  Therefore type inventory, age stationarity, and
quotient component count no longer force a literal sidecar.

Before fusion there are at most `3q` constituent cycles, so the proof uses
at most `3q-1` type-level merges.  Lemma 3.4 implies that a repair-first
literal realization would need the same order of colour-carrying `C6` or
longer packets, not transparent `C4`s.  For unbounded `q` this is outside
the fixed-small-protected-bank theorem.  The prospective construction of
the already fused word is therefore genuinely stronger than post-hoc
switching a frozen Catalan factor.

The physical lift is still not automatic.  Theorem 6A.1 should be applied
*before* choosing the owner chronology; trying to realize its two-edge
merges as post-hoc Johnson `C4` switches conflicts with Lemma 3.4.  The
smallest proof-safe prospective construction is:

1. form the fused type word of Theorem 6A.1;
2. choose an owner-simple protected Catalan/quotient cycle jointly with
   that word;
3. solve the resulting guard-pruned layered age-partition path, with the
   deleted owner coordinate in the oldest class at every step; and
4. impose the lower/upper/common-cap occurrence rows on that same path.

Once the owner cycle, root and fused type word are fixed, Step 3 alone is a
unit-flow/reachability problem in a layered digraph and is integral.  Step
4 is the genuine correlated coloured-path gate; separate rankwise stock or
same-owner biregularity does not imply it.

### Theorem 6A.2 (exact owner-moving protected-host criterion)

Let

```text
T_0,T_1,...,T_(M-1)
```

be a simple cyclic Johnson order of rank-`r` owners.  On edge `i`, write

```text
T_(i+1)=T_i-{alpha_i}+{beta_i}.
```

Let `c_i` be the fused positive-terminal type word from Theorem 6A.1, in
the same cyclic order.  For each layer `i`, let `P_i` be the set of ordered
partitions

```text
P=(C_0,...,C_d) of T_i,
|C_j|=(c_i)_j,          alpha_i in C_d.              (6A.3)
```

Join `P in P_i` to `P' in P_(i+1)` when

```text
C'_(j+1) subseteq C_j             (0<=j<d).          (6A.4)
```

Then the owner/type pair has a literal cyclic source realization if and
only if the cyclic layered graph (6A.3)--(6A.4) has a transversal directed
cycle selecting one state in every layer.

Every such realization:

1. uses every listed owner exactly once;
2. realizes the prescribed fused age type at every owner;
3. has no finite (equivalently, zero-delimited) cyclic positive
   owner-coordinate run shorter than `d+1`; constant all-one coordinates
   are harmless; and
4. uses no actuator sidecar beyond the standard `d`-letter collar needed
   to open a cyclic word.

For an opened owner path, impose `alpha_i in C_d` only at layers having an
actual outgoing Johnson edge.  The final layer is unrestricted unless a
prescribed exterior seam supplies its deletion label.  After the two
endpoint partitions/collars are fixed, existence is ordinary source--sink
reachability.  Endpoint-clipped positive runs may of course be shorter.

#### Proof

A literal trace window determines its most-recent-occurrence partition.
The deleted owner coordinate cannot occur in any retained source letter,
so Lemma 4.1 puts `alpha_i` in `C_d`; every survivor advances by one age,
which is (6A.4).  This proves necessity.

Conversely, for one selected edge define the next age-zero class by the
owner-moving formula (4.2).  Its size is `(c_(i+1))_0`, it is disjoint from
the selected survivors, and their union is `T_(i+1)`.  Hence the selected
partition cycle spells the nonempty source letters `C^i_0` and has exactly
the desired consecutive full-window owners and types.

A coordinate born on an insertion edge begins in age zero.  It cannot be
deleted until it lies in the oldest class `C_d`, at least `d` further
shifts later.  Thus every cyclic run having a birth and death has length at
least `d+1`; a coordinate present throughout the cycle has no finite
zero-delimited run.  The cyclic spelling has `M` phase letters.  Writing it
linearly repeats the usual initial `d` letters at the end (or equivalently
uses the standard opening collar), but the actuator adds no further
sidecar.  Removing the wrap edge gives the path statement with the endpoint
qualifications above.  \(\square\)

The theorem is an exact protected-host *criterion*, not an existence proof.
Deleting states/arcs that hit fixed owner, residence, upper-witness, or
local common-cap guards is sound.  Global all-different palettes and a
common matching must either be carried in an enriched state or imposed on
the same selected path; their marginal Hall systems alone do not imply a
common transversal cycle.

There is nevertheless an unconditional local owner-moving lift.

### Theorem 6A.3 (strict-positive open-path lift)

Let

```text
c^0 -> c^1 -> ... -> c^ell
```

be any legal age-type path with

```text
ell<=d,       c^t_i>=1 for every t,i,       k-r>=ell. (6A.5)
```

Then there are pairwise distinct Johnson-adjacent rank-`r` owners

```text
T_0,T_1,...,T_ell
```

and compatible literal age partitions of types `c^0,...,c^ell`.
The `ell` rank-`r-1` intersections are pairwise distinct, and so are the
`ell` rank-`r+1` unions.
Consequently every constituent cycle of the arbitrary-hole parity-sweep
packet becomes, after cutting one edge, an owner-simple literal open path
whenever `k-r>=d`.  It has no internal positive owner run shorter than
`d+1`; only its two clipped endpoint states remain for the ambient collar.

#### Proof

Choose distinct coordinates

```text
alpha_0,...,alpha_(ell-1) in T_0
```

and put `alpha_t` in initial age class `d-t`.  These classes are distinct,
and every class has positive capacity by (6A.5).  Fill the remaining class
positions arbitrarily.  Choose distinct fresh coordinates

```text
beta_0,...,beta_(ell-1) outside T_0
```

and define

```text
T_(t+1)=T_t-{alpha_t}+{beta_t}.                       (6A.6)
```

No inserted `beta_t` is later deleted.  Hence the owners in (6A.6) are
pairwise distinct.

The transition at time `t` has lower and upper colours

```text
K_t=(T_0-{alpha_0,...,alpha_t})
       union {beta_0,...,beta_(t-1)},
U_t=(T_0-{alpha_0,...,alpha_(t-1)})
       union {beta_0,...,beta_t}.                    (6A.7)
```

Because the `alpha` and `beta` banks are disjoint, the number of retained
initial coordinates in either formula determines `t`.  Thus both colour
families are pairwise distinct.

At time `u`, every future deletion `alpha_t`, `t>=u`, has age

```text
                         d-t+u.                       (6A.8)
```

These ages are distinct.  Delete `alpha_u` from the oldest class.  In each
younger class include its at most one future deletion token among the
survivors.  This is possible because every target age class has capacity at
least one; fill the remaining survivor quota arbitrarily, using the legal
inequalities

```text
(c^(u+1))_(i+1)<=(c^u)_i.
```

Formula (4.2) then supplies the next age-zero class and owner.  Induction
constructs all partitions.

To realize the initial partition literally, take the preceding `d+1`
source letters to be its age classes in reverse chronological order.  The
update formula then spells the rest of the open path.  Every deletion token
is oldest when deleted, and every newly inserted token remains through the
right endpoint; hence no short run is wholly internal.  Equivalently,
Theorem 6A.2's age argument gives internal run floor `d+1`.  \(\square\)

This theorem places each bounded actuator body on fresh owners.  It does
not make different bodies' lower intersection colours distinct, preserve
upper/common-cap tickets, or join their endpoint states.  Applying the
small protected-factor theorem is therefore valid only for a fixed number
of already resource-disjoint strands satisfying its edge budget; it does
not stock an unbounded multiplicity block.

Owner and immediate-palette disjointness can in fact be imposed
simultaneously by a direct counting argument.

### Theorem 6A.4 (dispersed protected open-strand reservoir)

Let

```text
W_0=binom(k,r),   W_-=binom(k,r-1),   W_+=binom(k,r+1).
```

Fix `Q` prescribed strict-positive legal age paths, each of length at most
`d` transitions, and assume `k-r>=d`.  Let fixed forbidden banks contain
`f_0` rank-`r` owners, `f_-` rank-`r-1` lower colours, and `f_+`
rank-`r+1` upper colours.  Put

```text
eta=(d+1)^2/W_0 + d^2/W_- + d^2/W_+,
theta=f_0(d+1)/W_0 + f_-d/W_- + f_+d/W_+.            (6A.9)
```

If

```text
                         theta+(Q-1)eta<1,            (6A.10)
```

then all `Q` paths have literal lifts as in Theorem 6A.3 whose owner,
lower-colour and upper-colour sets are pairwise disjoint and avoid the
three forbidden banks.

#### Proof

For a path of length `ell`, use every choice of initial owner, ordered
distinct deletion bank in that owner, and ordered distinct insertion bank
outside it.  The number of monotone owner paths is

```text
N_ell=W_0 (r)_ell (k-r)_ell.                          (6A.11)
```

Theorem 6A.3 lifts each one to the prescribed age path.  The symmetric
group is transitive on each rank, and the resources inside one path are
distinct.  Double-counting resource incidences therefore gives exactly

```text
N_ell(ell+1)/W_0     paths through a fixed owner,
N_ell ell/W_-        paths through a fixed lower colour,
N_ell ell/W_+        paths through a fixed upper colour. (6A.12)
```

Equivalently, a uniformly chosen candidate path has the exact
one-resource incidence probabilities

```text
Pr[T is an owner on the path]=(ell+1)/W_0,
Pr[K is a lower colour on the path]=ell/W_-,
Pr[U is an upper colour on the path]=ell/W_+.        (6A.13)
```

No independence is used: the proof below applies only the union bound to
these exact marginals.

The union bound and `ell<=d` show that the fixed forbidden bank removes at
most `theta N_ell` candidates.  Each previously selected path removes at
most `eta N_ell` further candidates.  Before the `q`th greedy choice, the
discarded fraction is at most `theta+(q-1)eta<1`; hence a candidate
remains.  Induction selects all `Q` lifts.  \(\square\)

In the odd middle-levels setting `k=2r-1`, the incidence lift of these
paths is a 2-bounded protected bank with exactly

```text
                         2 sum_a ell_a               (6A.14)
```

incidence edges.  Therefore the small protected-factor theorem embeds the
whole bank in a spanning owner/lower two-factor whenever

```text
                         2 sum_a ell_a<=r-2.          (6A.15)
```

This is a genuine protected-factor placement theorem for every library
meeting the explicit budget.  It does not say that the factor extension
joins the strands in the fused type order, preserves residence across the
new endpoint edges, or even extends the chosen source-letter traces through
those endpoint edges.  Nor does it cover the upper palette outside the
protected bank, deeper upper shadows, or one common-cap compiler.  If an
`O(d)` library has total path length larger than the linear budget (6A.15),
a prospective global Catalan construction is still necessary.

### Corollary 6A.5 (one arbitrary-hole packet in a protected factor)

One arbitrary-hole parity-sweep packet has at most three constituent
cycles.  After cutting one edge in each, it has at most three paths and
total transition length at most `3d`.  Therefore, if

```text
k-r>=d,                 6d<=r-2,
theta+2eta<1,                                           (6A.16)
```

then its complete local owner/lower/upper-disjoint open-strand bank can be
chosen avoiding the fixed resources and embedded in a spanning
owner/lower two-factor.

This stocks the full `O(d)`-role **open-body bank** without appending
literal owners.  It is not yet a completed physical actuator: the cut
transitions and guarded endpoint joins are absent.  It does not stock an
unbounded multiplicity of that packet, and the factor supplied by the
extension theorem need not implement the fused type order.

## 7. Exact prospective flow criterion

For completeness, the stock selection in a *given* protected occurrence
catalogue has an ordinary integral formulation under the explicit
**role-Markov/interchangeability** hypothesis: after the current typed role
is known, future legality and payload do not depend on which named source
copy reached it, and only aggregate typed exit counts are prescribed.

For every actuator kind, hole position and stage in its named path, make a
separate role layer.  Copy every clean candidate occurrence into the role
layers it is allowed to fill, but route all copies through one shared
unit-capacity occurrence arc.  Add transition arcs only between consecutive
named stages of `S_j`, `T_j`, or the parity-sweep body, and only when the
literal transition is owner-legal and passes all declared local guards.
Put the required integral supply at the typed first roles and the matching
demand at the corresponding typed last roles.  Under interchangeability,
the standard open-body stock exists exactly when this role-expanded
node-capacitated network has the prescribed integral flow.

By max-flow integrality, fractional feasibility is sufficient.  By
max-flow/min-cut, failure has the exact certificate

```text
capacity(delta^+(S))
  < total actuator supply trapped in S.               (7.1)
```

Without the role expansion, a generic occurrence graph is only a
relaxation: it may skip stages or splice pieces from incompatible actuator
types.  With the expansion, the criterion selects vertex-disjoint open
actuator bodies under the stated interchangeability hypothesis.  If a
named source must reach a named sink, or a carried upper/common-cap payload
depends on its earlier choices, this becomes a coloured disjoint-path/
multicommodity problem and ordinary max-flow is again only a relaxation.
It becomes a
zero-sidecar physical theorem only after the selected bodies possess the
phase-transparent entry rectangles and guarded component fusion in Section
6.  Without that extra state, (7.1) is merely an occurrence-reservoir
packing theorem.

## 8. Corrected all-`k` frontier

The uniform algebra now has a precise split.

* **Solved:** single/double actuator type inventory is `O(d)`; its exact
  multiplicity stock is laminar; and every abstract cycle copy can be fused
  into one type cycle.
* **Refuted with exact cost `U-1`:** direct stocking of the older
  single-hole cycle in a flat one-copy protected Catalan chronology.  The
  empty oldest class in `B_j` forces one block endpoint per repair.  This
  rules out a dimension-uniform `O(1)` sidecar whenever the required
  multiplicity `U(k)` is unbounded.
* **Solved at quotient level by the later parity sweep:** arbitrary hole
  sets now have a positive-terminal `O(d)`-type packet, and all packet
  copies fuse into one type-occurrence cycle.
* **Still open physically:** a jointly chosen owner chronology and
  occurrence-labelled partition path carrying that fused word, with a
  colour-carrying `C6`/longer mechanism or direct prospective construction,
  and protected upper/common-cap payload.

No statement here proves a protected Catalan host, a common-cap compiler,
`B(k)+O(1)`, or `nu(k)=B(k)`.

## 9. Independent audit

An independent proof audit checked the stock formula (2.1), common-entry
fusion, Lemma 3.4, the departure/converse formulas (4.1)--(4.2), and the
block lower bound (5.2).  It required three scope corrections now included
above: `c_d=0` is an empty **oldest** class, the finite `k=54` cost does not
alone refute an unspecified absolute constant, and the prospective flow in
Section 7 must be role/layer expanded.

A second independent audit compared Section 6A against the arbitrary-hole
parity-sweep construction.  It verified the sharper terminal values

```text
(R_p)_d=2 iff p=d,
(Y_(a,u))_d=2 iff a=1,
(X_m)_d=2 iff m=1,
```

with value one otherwise, and confirmed that occurrence-distinguished
common-`D` outgoing switches merge every constituent cycle while retaining
all vertex-attached marked payloads.  No additional mathematical correction
was required.  It also audited Theorem 6A.2 and supplied the three endpoint
scope qualifications now stated there: constant cyclic coordinates are
harmless rather than short, linearization uses the standard `d`-letter
opening collar, and an open path's last layer needs no deletion label unless
an exterior seam prescribes one.

The same audit independently checked Theorems 6A.3--6A.5.  It verified the
pre-aged deletion invariant, both palette formulas, the exact candidate
count `W_0(r)_ell(k-r)_ell`, all three resource-incidence marginals,
`theta/eta`, the greedy inequality, the `2 sum ell_a` incidence-edge count,
and the one-packet constants `3d,6d`.  Its only wording correction—now
made—is that Corollary 6A.5 stocks an open-body bank, not the still-unjoined
physical actuator.
