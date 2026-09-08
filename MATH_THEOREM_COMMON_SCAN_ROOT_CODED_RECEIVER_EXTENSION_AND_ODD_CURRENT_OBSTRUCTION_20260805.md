# A common coordinate scan absorbs a whole root-coded receiver bank

**Date:** 2026-08-05  
**Method:** co-design the prescribed receiver edges and the completing
matching; no computation  
**Status:** unconditional on the labelled even capacity-two sector, and
on every necklace sector with trivial background stabilizer.  A fixed
root-coded receiver bank can be planted as parallel copies of one local
edge and then deleted from one common perfect matching.  This removes all
post-hoc proper Hall cuts for that bank.  The analogous rooted nonwrap
construction at odd coordinate length is impossible with one parity
socket: it retains the exact macroscopic wrap-current obstruction.

## 1. The scan matching with prescribed rows

Let

\[
 \mathcal T_{2m,R}
 =\{t\in\{0,1,2\}^{\mathbb Z_{2m}}:\sum_i t_i=R\},
 \qquad R\text{ odd}.
\tag{1.1}
\]

Choose one of the two perfect matchings of the coordinate cycle and
order its coordinate pairs

\[
                         p_1,p_2,\ldots,p_m.
\tag{1.2}
\]

On each pair choose one of the local rows

\[
\begin{array}{c|c|c}
\text{local mass}&\text{selected local edge}&\text{quiet state}\\ \hline
0&\varnothing&00\\
1&01-10&\varnothing\\
2&20-11&02\\
2&02-11&20\\
3&12-21&\varnothing\\
4&\varnothing&22.
\end{array}
\tag{1.3}
\]

The associated scan matching acts at the first nonquiet pair.

### Theorem 1.1 (triangular quiet-prefix extension)

For each `i`, let `F_i` be a family of literal token edges supported on
`p_i`.  Suppose that

1. the restriction of every edge in `F_i` to `p_i` is the selected
   local edge in (1.3); and
2. for every `j<i`, the common restriction of the two endpoints of every
   edge in `F_i` to `p_j` is quiet.

Then the scan perfect matching contains every edge in

\[
                              F=\bigcup_i F_i.
\tag{1.4}
\]

In particular, the edges in `F` are automatically pairwise
vertex-disjoint.

#### Proof

Take `e in F_i`.  Its two endpoints agree on every pair other than
`p_i`.  By hypothesis every earlier pair is quiet.  At `p_i` the two
endpoints form the chosen nonquiet local edge.  Thus the first nonquiet
pair of either endpoint is `p_i`, and the scan involution exchanges the
two endpoints of `e`.  This holds for every `e in F`.

The scan rule is a function and an involution, so two distinct contained
edges cannot share an endpoint. \(\square\)

The most useful case has no triangular bookkeeping at all.

### Corollary 1.2 (one-row common base)

Fix one coordinate pair `p` and put it first.  Every family of literal
edges supported on `p` and using one fixed local row of (1.3) lies in one
perfect matching of `T_(2m,R)`.

Thus literal edge extendability is simultaneously true for an arbitrary
number of parallel contextual copies of the same local edge, not merely
one prescribed edge.

## 2. Deleting the common base closes every receiver cut

Let `G` be an even labelled sector and let `F={a_jb_j:j in J}` be a
family of selected receiver-pair edges.  Suppose one perfect matching
`M` of `G` contains `F`.

### Theorem 2.1 (common-base receiver extension)

After deleting all receiver endpoints, the graph has the perfect
matching

\[
                               M\setminus F.
\tag{2.1}
\]

Equivalently, in the augmented receiver graph, replacing every edge
`a_jb_j in F` by the two terminal edges

\[
                    \alpha_j a_j,\qquad \beta_j b_j
\tag{2.2}
\]

gives a perfect matching.  Hence every augmented Hall inequality,
including every trapped-square proper cut, holds automatically.

If an incoming singleton `i` and an outgoing socket `o` are also the
endpoints of one edge `io in M` disjoint from `F`, then

\[
                         M\setminus(F\cup\{io\})
\tag{2.3}
\]

matches the remaining ordinary vertices.  Thus a regeneratively chosen
socket may be installed as one more parallel common-row edge.

#### Proof

A matching containing `F` uses no other edge at an endpoint of `F`.
Deleting those endpoints therefore deletes exactly the edges `F` from
`M`, proving (2.1).  The replacement (2.2) is the literal equivalence in
the augmented matching theorem.  The socket statement is identical.
\(\square\)

This theorem is stronger than proving the receiver Hall cuts after the
bank has been frozen: it chooses the bank and its completing base in one
step.

## 3. Root-coded banks can be made parallel

There is a direct capacity-two construction, independent of any
post-hoc receiver catalogue.  Reserve coordinate pairs `p_0,p_1,p_2`
and a further block of `s` coordinate pairs.  Choose `q` distinct binary
words `c_f in {0,1}^s` of one fixed weight `w`; thus

\[
                              q\le {s\choose w}.
\tag{3.1}
\]

For every codeword make four states `v_(alpha beta)^f` as follows:

\[
\begin{array}{c|c}
\text{pair}&\text{local state}\\ \hline
p_0&12\text{ if }\alpha=0,\quad21\text{ if }\alpha=1,\\
p_1&12\text{ if }\beta=0,\quad21\text{ if }\beta=1,\\
p_2&10,\\
\text{code pair }j&22\text{ if }c_f(j)=1,\quad00\text{ otherwise}.
\end{array}
\tag{3.2}
\]

Put the same fixed local states on all unused pairs.  The four displayed
states have common odd mass

\[
                              R=7+4w+R_0,
\tag{3.3}
\]

where the fixed filler mass `R_0` is even.  The `p_0` and `p_1` moves
commute, so the four states form a literal receiver `K_(2,2)`.  The
selected side

\[
                         e_f=v_{00}^f v_{10}^f
\tag{3.4}
\]

is always the local edge `12-21` on `p_0`.  Different codewords give
vertex-disjoint squares.  In the macro interpretation, deleting either
active boundary merges residues `(5,0)` or `(0,5)` to residue five, so
these are ordinary critical parent-petal receiver squares, not merely
abstract token edges.

There are `u=m-s-3` unused pairs.  Fixed filler pairs `00,20,22` realize
every even filler mass from zero through `4u`.  Thus the construction is
available for every odd `R` in the exact interval

\[
 7+4w\le R\le
 7+4w+4(m-s-3)
   =4m-4(s-w)-5.
\tag{3.5}
\]

Complementing every digit gives the reflected interval.  Hence, for fixed
`q` (and therefore fixed `s,w`), every central odd sector contains the
bank for all sufficiently large `m`.

This fixed-weight code is already a literal root once an aperiodic
background is chosen in Section 4.

There is an important scope distinction.  The previously proved
protected gap-marker/workspace bank lives natively in the hook angle
family, whose vacancy-circle length is odd.  Fixed marker weight does
show that its selected sides are formal parallel contextual copies, but
that theorem alone does **not** transplant the bank into an even-coordinate
odd-mass sector.  The even bridge used below is instead the direct
capacity-two construction (3.1)--(3.4).

### Theorem 3.1 (parallel root-coded receiver bank)

The explicit construction (3.1)--(3.4) gives `q` receiver tasks whenever
there are at least `s+3` coordinate pairs and the prescribed odd mass has
the displayed filler.  Separately, the old protected hook bank exists
under its root-code slack condition

\[
 k\ge s+3,
 \qquad
 \ell-3k\ge s+w+12
\tag{3.6}
\]

but its odd completion is governed by Section 5.  For the direct even
bank, one task per coded context has a selection whose literal edges are
all contained in one coordinate-scan perfect matching of the compatible
even labelled capacity-two sector.

Consequently the selected receiver bank has an exact residual perfect
matching; no invisible-bicycle or proper-cut estimate is required.

#### Proof

Formula (3.2) proves literally that the squares are disjoint and that
every selected edge is the same local row on `p_0`.  Put that pair first.
Corollary 1.2 gives the common perfect matching, and Theorem 2.1 gives the
residual matching. \(\square\)

The construction uses one coded hub per receiver task.  This is the
important quantifier change: multiple tasks need not first be generated
over one frozen hub and then routed through an arbitrary residual graph.

## 4. Necklace descent by background co-selection

In the capacity-two decomposition, a background word `a` leaves the
quotient group `Stab(a)`.  If `a` is aperiodic, this stabilizer is trivial,
so the necklace sector is literally the labelled sector.  The common
scan then descends without any equivariance argument.

### Corollary 4.1 (quotient-safe common scan)

Theorem 3.1 holds verbatim in every aperiodic background sector.  In
particular, whenever the total background mass is `A>0`, the background

\[
                         a=(A,0,\ldots,0)
\tag{4.1}
\]

has trivial stabilizer and supports the construction.

For a fixed finite list of sectors which must be kept separate, choose
`A>2q` and

\[
                 a^{(f)}=(A-f,f,0,\ldots,0),
                 \qquad 1\le f\le q.
\tag{4.2}
\]

These have the same total mass, are pairwise rotation-inequivalent, and
have trivial stabilizer.  Thus a fixed bank may alternatively be split
among independent quotient sectors, one common-scan completion per
sector.

#### Proof

In (4.1) the unique positive coordinate fixes every stabilizing rotation.
In (4.2), `A-f>f` is the unique maximum; aligning it leaves the following
entry `f`, so two different values of `f` are not rotations.  The
capacity-two residue graph is independent of the background values, so
the same receiver geometry is available in every sector. \(\square\)

This separates ordinary vertices from a fixed earlier bank by background
sector.  It does **not** by itself separate deleted-cut hub colours:
merging two coordinates can make edges from different child backgrounds
share one parent colour.  Avoiding the two reset colours therefore needs
either an independently checked hub-colour separation or the following
co-selection lemma.

### Theorem 4.2 (finite merged-colour avoidance)

Fix an even coordinate length `n>=4`, a total background mass `A`, and a
family `C` of `c` forbidden cyclic parent-background words of length
`n-1` and mass `A`.  If

\[
 {A+n-1\choose n-1}
  > c n(n-1)(A+1)
    +\sum_{\substack{d\mid n\\d<n}}
       {A+d-1\choose d-1},
\tag{4.3}
\]

then there is an aperiodic child background `a in N^n` of mass `A` such
that no adjacent merge of `a` is a rotation of a member of `C`.

Consequently, for every fixed reset-colour bank and fixed coordinate
length `n>=4`, all sufficiently large background masses admit one
aperiodic common-scan sector in which **no** scan edge has a forbidden
reset colour.

#### Proof

There are `{A+n-1 choose n-1}` weak compositions `a` of mass `A`.  Fix a
boundary, a forbidden cyclic word, and one of its `n-1` rotations.  To
invert the adjacent merge, split one specified target entry into two
nonnegative parts.  This has at most `A+1` solutions.  Thus all forbidden
merge preimages together number at most `c n(n-1)(A+1)`.

If `a` has a proper period `d|n`, it is determined by `d` entries; ignoring
the additional divisibility restriction gives at most
`{A+d-1 choose d-1}` possibilities.  The second term in (4.3) therefore
upper-bounds all periodic backgrounds.  Under (4.3) some composition is
neither periodic nor a forbidden merge preimage.  Background is part of
the deleted-cut colour, so every scan edge in its sector avoids `C`.
\(\square\)

The left side of (4.3) has degree `n-1` in `A`, while the reset term has
degree one and every periodic term has degree at most `n/2-1`.  Hence the
asymptotic consequence is literal.  The corollary still makes no claim on
the zero-background periodic sector.

## 5. The odd hook cannot use the same one-socket scan

Now let the coordinate length be `2m+1`, root the wrap boundary, and use
only nonwrap coordinate-pair scans.  For odd mass `R`, the rooted path
shore imbalance is

\[
 \Delta_{m,R}
   =[z^{R-1}](1+z^2+z^4)^m.
\tag{5.1}
\]

### Theorem 5.1 (fixed-bank odd scan obstruction)

Let `F` be any fixed bank of `q` prescribed receiver edges.

1. If every edge of `F` is nonwrap, then every completion using only
   nonwrap edges leaves at least `Delta_(m,R)` ordinary vertices
   unmatched.  One parity socket changes this lower bound by at most one.
2. If `F` contains wrap edges, then even after orienting all of them on
   the majority shore, every nonwrap completion with one socket leaves at
   least

   \[
                         \Delta_{m,R}-2q-1
   \tag{5.2}
   \]

   unmatched vertices.

Therefore no fixed finite root-coded bank plus one parity socket can turn
the odd hook sector into the even common-scan theorem whenever
`Delta_(m,R)>2q+1`.  At central odd mass this obstruction is unbounded.

#### Proof

Every nonwrap edge crosses the rooted parity shores, so selecting or
prescribing such an edge removes one vertex from each shore and does not
change their difference.  A socket removes one vertex and changes the
difference by at most one.

A wrap edge lies within one shore and changes the signed difference by
exactly two.  Hence `q` prescribed wrap edges can change its absolute
value by at most `2q`.  Every remaining nonwrap matching leaves at least
the residual shore imbalance.  This proves both statements. \(\square\)

For the hook root-code family the vacancy-circle length is odd, so this
is the relevant parity.  Allocating finitely many receiver tasks to
independent hook sectors does not remove the obstruction: each central
sector separately needs its own macroscopic wrap/circulation current.

The correct odd analogue of Theorem 3.1 must therefore co-select

1. the fixed parallel receiver bank;
2. a bank of order `Delta_(m,R)/2` majority-shore wrap or circulation
   ears; and
3. the one residual parity socket,

inside one near-perfect matching.  A bounded receiver bank cannot replace
item 2.

## 6. Exact scope

Proved:

1. a general triangular quiet-prefix criterion for prescribing many
   edges in one even coordinate scan;
2. the stronger one-row common-base theorem;
3. a root-coded construction placing one receiver task per hub in that
   one row;
4. exact residual receiver completion, including a co-designed socket
   edge, by deleting the common base;
5. quotient descent on aperiodic co-selected backgrounds and separation
   into finitely many such sectors; and
6. an exact odd one-socket obstruction of size
   `Delta_(m,R)-2q-1`.

Not proved:

1. descent of the common scan in the zero-background periodic sector;
2. bounded-background-mass and zero-background cases where the finite
   merged-colour avoidance inequality is unavailable;
3. the macroscopic odd wrap/circulation-ear common base;
4. regeneration of the chosen aperiodic background sectors across every
   Pascal/PBBS level; or
5. the complete all-dimensional receiver theorem.
