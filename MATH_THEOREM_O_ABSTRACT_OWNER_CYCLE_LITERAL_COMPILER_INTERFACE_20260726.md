# Abstract owner cycles compile literally without wreaths

## Exact atom identities, component collars, leaves, tails, and parity

Date: 2026-07-26

Method: pure mathematics only.  No finite search, computation, solver, or
web input is used.

## 0. Outcome

The interface warning has a clean resolution.

An owner cycle does **not** have to be a wreath, have length equal to the
ground-set size, arise from an odd-graph cycle, or carry an omitted-label
permutation.  Arbitrary cyclic rows of actual middle sets compile directly
to a literal contiguous-OR word.  The only local input is a positive-dwell
condition for the coordinate state rows; geodesicity supplies the intended
shadow ranks.  The only global inputs are the number of components and the
**actual** missing lower and upper targets.

For an even ground set of size `2m`, let

\[
                         W_m=\binom{2m}{m}.
\tag{0.1}
\]

Suppose an owner-disjoint family of cyclic middle rows contains `G` owners
and has `K` components.  At depth `d<m`, assume the literal delay condition
and rank-correct lower and upper traces stated in Section 2.  Let

\[
 \Delta_d=\sum_{q=1}^{d}(M_q^-+M_q^+)
\tag{0.2}
\]

be the aggregate number of actual missing targets in the two signed central
shadows.  Then the exact finite bound is

\[
 \boxed{
 \nu(2m)\le
 W_m+2dK+\Delta_d+L_m(m-d-1).}
\tag{0.3}
\]

Here `L_m` is the explicit two-tail product-SCD length in Section 5.  The
owner leave `u=W_m-G` has disappeared from (0.3) for an exact reason: the
atom blocks cost `G`, and appending the `u` missing middle owners changes
this to exactly `W_m`.  The term `2dK` is the whole component/seam toll.
There is no connector, separator, or intercomponent seam charge.

Consequently

\[
 {d\over\sqrt m}\longrightarrow\infty,
 \qquad K=o(W_m/d),
 \qquad \Delta_d=o(W_m)
\tag{0.4}
\]

imply

\[
                         \nu(2m)=(1+o(1))W_m.
\tag{0.5}
\]

In particular, if all retained cycles have length at least `c m` for one
fixed `c>0`, then `K<=W_m/(c m)`.  Thus every choice

\[
                         \sqrt m\ll d\ll m
\tag{0.6}
\]

makes the complete collar `2dK=o(W_m)`.  The cycles may have mutually
different lengths `Theta(m)`; none need have length `2m` or `2m+1`.

Ordinary cyclic Johnson `H`-geodesicity supplies the delay condition only
through depth `H-1`.  Hence the safe off-by-one specialization of (0.3) is

\[
 \boxed{
 \nu(2m)\le W_m+2(H-1)K+
 \sum_{q=1}^{H-1}(M_q^-+M_q^+)+L_m(m-H).}
\tag{0.7}
\]

Full depth `H` follows from geodesicity through `H+1`, or from separately
checking the positive-dwell condition at depth `H`.

The usual trimmed one-bit lift has exact length `2 nu(2m)` and transfers
(0.5) to odd dimensions with coefficient one.  There is also a direct
odd-dimensional theorem in Section 7.  Its only extra warning is decisive:
for arbitrary Johnson owner rows, upper holes must be counted separately.
The equality between upper holes and complementary lower holes is special
to an odd-graph parity double cover (or another separately proved duality).
It is not a consequence of geodesicity and is not used in the even theorem.

Thus no wreath-conversion statement is needed.  If an upstream theorem
already gives actual owner-disjoint safe Johnson cycles with (0.4), the
constant-one implication is complete.  If it gives only abstract cycles,
rank-correct flags not realized by consecutive set intersections/unions, or
only a one-sided hole estimate, that literal-state/two-sided-support step is
the exact missing conversion.

## 1. Literal OR words and cyclic rows

For a finite ground set `V`, a literal word is a finite sequence

\[
                         Q=(Q_1,\ldots,Q_N)
\tag{1.1}
\]

of nonempty subsets of `V`.  It covers `S` if

\[
                         S=Q_i\cup Q_{i+1}\cup\cdots\cup Q_j
\tag{1.2}
\]

for some `i<=j`.  Let `nu(|V|)` be the minimum length of a word covering
every nonempty subset of `V`.

Let

\[
                         C=(X_i)_{i\in\mathbb Z/\ell\mathbb Z}
\tag{1.3}
\]

be a cyclic row of distinct `m`-subsets of a ground set.  No fixed value of
`ell` is imposed.  For a coordinate `v`, its state row is the cyclic binary
word

\[
                         (\mathbf1_{v\in X_i})_i.
\tag{1.4}
\]

### Definition 1.1 (positive delay)

The row satisfies `P_d` if every nonconstant positive run in every state
row (1.4) has at least `d+1` consecutive states.  A coordinate present in
every `X_i` is allowed.

Define the cyclic delayed atoms

\[
                         B_j=\bigcap_{s=0}^{d}X_{j-s}.
\tag{1.5}
\]

The atoms are literal subsets of the original ground set.  They need not
be disjoint, distinct, or singleton sets.  Some may be empty; all empty
letters will be deleted after the witnesses have been identified.

## 2. The universal delay identities

For `0<=q<=d`, put

\[
 L_{i,q}=\bigcap_{t=0}^{q}X_{i+t},
 \qquad
 U_{i,q}=\bigcup_{t=0}^{q}X_{i+t}.
\tag{2.1}
\]

### Lemma 2.1 (exact atom identities)

If `C` satisfies `P_d`, then, with all indices cyclic,

\[
 \boxed{X_i=\bigcup_{j=i}^{i+d}B_j,}
\tag{2.2}
\]

\[
 \boxed{L_{i,q}=\bigcup_{j=i+q}^{i+d}B_j,}
 \qquad 0\le q\le d,
\tag{2.3}
\]

and

\[
 \boxed{U_{i,q}=\bigcup_{j=i}^{i+d+q}B_j,}
 \qquad 0\le q\le d.
\tag{2.4}
\]

These identities use no adjacency, geodesicity, cycle-length, wreath, or
factor hypothesis.

#### Proof

Fix a coordinate `v`.  Consider first a nonconstant positive run, lifted
from the cyclic index set to an integer interval `[a,b]`.  Its length is at
least `d+1`.  By (1.5), the atoms containing `v` are exactly those with
right endpoint

\[
                         j\in[a+d,b].
\tag{2.5}
\]

If `v in X_i`, then `i in[a,b]`, and

\[
                         [a+d,b]\cap[i,i+d]\ne\varnothing.
\tag{2.6}
\]

Thus one of `B_i,...,B_{i+d}` contains `v`.  Conversely every such atom is
an intersection containing `X_i` among its defining states whenever it is
used for `i`; coordinatewise this proves (2.2).

If `v in L_{i,q}`, then `[i,i+q]` lies in one positive run.  Now

\[
                         [a+d,b]\cap[i+q,i+d]\ne\varnothing,
\tag{2.7}
\]

because `i+q<=b`, `a+d<=i+d`, and `q<=d`.  Conversely every atom indexed
between `i+q` and `i+d` is defined using all states `X_i,...,X_{i+q}`.
This proves (2.3) coordinatewise.  A coordinate present around the whole
cycle belongs to every relevant state and atom, so the same argument is
automatic for constant positive rows.

Finally take the union of (2.2) for
`X_i,X_{i+1},...,X_{i+q}`.  The union of their atom-index intervals is
exactly `[i,i+d+q]`, proving (2.4). \(\square\)

### Definition 2.2 (rank-correct safety)

On a row of `m`-sets, write `G_d` for the condition

\[
 |L_{i,q}|=m-q,
 \qquad
 |U_{i,q}|=m+q
 \quad(0\le q\le d,\ \text{all }i).
\tag{2.8}
\]

For a Johnson walk, this is equivalent to every segment of at most `d`
transitions being geodesic: all \(2q\) toggled coordinates in every
\(q\)-transition segment are distinct.  Equivalently, the deleted
coordinates are distinct, the inserted coordinates are distinct, and the
two sets are disjoint; this excludes both insertion-then-deletion and
deletion-then-reinsertion returns.

### Lemma 2.3 (the precise geodesic/delay off-by-one)

For a cyclic Johnson row,

\[
                         G_h\Longrightarrow P_{h-1}.
\tag{2.9}
\]

In particular `G_(d+1)` implies `G_d+P_d`.

#### Proof

Suppose a nonconstant positive run of coordinate `v` has `r` states.
The path beginning immediately before the insertion of `v` and ending
immediately after its deletion has `r+1` transitions.  It inserts and then
deletes the same coordinate, so its endpoint Johnson distance is strictly
less than `r+1`; it is not geodesic.  Under `G_h` this forces `r+1>h`, or
`r>=h`.  This is `P_(h-1)`. \(\square\)

The converse is false: `P_d` controls residence time, while `G_d` also
forbids collisions among distinct insertion and deletion histories.  The
literal theorem therefore states the two properties separately and invokes
Lemma 2.3 only as a convenient sufficient package.

## 3. Exact linearization of one arbitrary-length row

Extend the atom indices periodically, `B_(j+ell)=B_j`, and emit

\[
 \boxed{
 B_0,B_1,\ldots,B_{\ell-1},B_0,B_1,\ldots,B_{2d-1}.}
\tag{3.1}
\]

For `d=0`, the copied part is empty.  Before deleting empty atoms, (3.1)
has exactly

\[
                         \ell+2d
\tag{3.2}
\]

letters.

### Lemma 3.1 (one-row literal compiler)

If the row satisfies `P_d`, the word (3.1) covers all sets in (2.1).
If it also satisfies `G_d`, those sets lie in the intended ranks `m-q`
and `m+q`.

#### Proof

Choose the representative `i in {0,...,ell-1}`.  Formula (2.3) uses the
atom interval `[i+q,i+d]`; formula (2.4) uses `[i,i+d+q]`.  The largest
possible right endpoint is `i+2d`, attained by the upper depth-`d` trace.
For `i=ell-1`, this is `ell+2d-1`, exactly the last index present in
(3.1).  Thus every cyclic atom interval has been linearized.

Delete all empty atoms from (3.1).  Each intended trace has size at least
`m-d>0`, so at least one atom in its witnessing interval is nonempty.
The surviving atoms from that interval remain consecutive, and their union
is unchanged.  Hence the resulting word is a legal nonempty literal word
of length at most (3.2). \(\square\)

The copied prefix in (3.1) is the exact support-blind collar required by
this construction.  The upper depth-`d` trace uses `2d+1` atoms, so a
cyclic interval beginning at the last base atom requires exactly `2d`
copied atoms.  This explains both the constant and the off-by-one.

No restriction `ell>=2d+1` is needed.  Periodic notation in (3.1) permits
the copied prefix to pass through the base row more than once.  Under
`G_d+P_d`, the familiar inequality `ell>=2d+1` is in fact automatic.
Choose a coordinate changed by one transition.  Its positive run has
length at least `d+1` by `P_d`.  Its nonconstant zero run has length at
least `d`: otherwise the path from the state immediately before deletion
to the state immediately after reinsertion would toggle that coordinate
twice in at most `d` transitions and would not be geodesic.  The two run
lengths sum to at most `ell`.  Thus `ell>2d`, exactly the auxiliary length
hypothesis sometimes attached to older versions of the compiler; it is not
an independent wreath-length assumption.

## 4. Global central compiler, owner leaves, and seams

Let `V` have size `2m`.  Let `mathcal C` be an owner-disjoint family of
cyclic rows satisfying `G_d+P_d`.  Put

\[
 G=\sum_{C\in\mathcal C}|C|,
 \qquad K=|\mathcal C|,
 \qquad u=W_m-G.
\tag{4.1}
\]

For `1<=q<=d`, let

\[
 M_q^-=\binom{2m}{m-q}
       -\left|\{L_{i,q}: i\text{ is a retained owner}\}\right|,
\tag{4.2}
\]

\[
 M_q^+=\binom{2m}{m+q}
       -\left|\{U_{i,q}: i\text{ is a retained owner}\}\right|.
\tag{4.3}
\]

These are support holes, not overloads and not labelled mismatches.  All
collisions have already been accounted for by taking image cardinality.

### Theorem 4.1 (exact factor-blind central word)

There is a literal word covering every rank in `[m-d,m+d]` of length at
most

\[
 \boxed{
 W_m+2dK+\sum_{q=1}^{d}(M_q^-+M_q^+).}
\tag{4.4}
\]

#### Proof

Concatenate the row words (3.1).  Their total length before empty deletion
is

\[
                         G+2dK.
\tag{4.5}
\]

Every witness certified in one row block remains an interval after
concatenation.  No witness crosses an interrow seam, so there is no seam
condition and no extra seam letter.  Cross-seam intervals may cover
additional targets and are simply ignored.

At rank `m`, the retained rows cover precisely their `G` owner sets.
Append each of the `u=W_m-G` missing middle owners once.  This changes
(4.5) to

\[
                         W_m+2dK.
\tag{4.6}
\]

For every positive depth, append each target counted in (4.2)--(4.3) once
as a literal set-letter.  This costs the last term in (4.4), and all ranks
in the band are covered. \(\square\)

This proves the exact owner-leave cancellation.  In particular `u` need
not be inserted as a further error term after the baseline `W_m`; doing so
would double count it.

The hypotheses of Theorem 4.1 are local to each retained row.  Different
rows may use unrelated chronologies, lengths, coordinate frequencies, and
frames.  The only coupling between rows is the support-hole number already
visible in (4.2)--(4.3).

### Corollary 4.2 (exact multicover correction)

More generally, let the cyclic rows form a multiset with total middle
occurrence mass \(P\).  Let

\[
 M_0=\#\{S:\mu_0(S)=0\},\qquad
 E_0=\sum_{|S|=m}(\mu_0(S)-1)_+ .
\tag{4.7}
\]

Then

\[
                              P+M_0=W_m+E_0,          \tag{4.8}
\]

and the same construction has central length at most

\[
 \boxed{
 W_m+E_0+2dK+\sum_{q=1}^{d}(M_q^-+M_q^+).}          \tag{4.9}
\]

#### Proof

The row blocks cost \(P+2dK\).  Appending the \(M_0\) missing middle
owners changes this to \(W_m+E_0+2dK\) by (4.8); the remaining repairs are
the actual signed holes. \(\square\)

The overload term is necessary.  Two identical copies of an exact safe
factor have no middle holes and need not have shadow holes, but have
\(E_0=W_m\) and leading length two.

### Theorem 4.3 (partial collars, paths, and bare-cut toll)

For every cyclic row \(C\), choose \(0\le\sigma_C\le d\), cut the row
once, and copy only its first \(\sigma_C\) owner states.  Apply the finite
delay construction to this linear row.  Before empty atoms are deleted its
formal length is

\[
                         |C|+d+\sigma_C.             \tag{4.10}
\]

At signed depth \(q\), exactly

\[
                         (q-\sigma_C)_+              \tag{4.11}
\]

cyclic starts on each sign are unavailable.  If
\(\Delta_d^{(\sigma)}\) is the actual aggregate signed target-hole count
after retaining only the available windows, then an owner-disjoint family
obeys

\[
 \boxed{
 \nu(2m)\le
 W_m+\sum_C(d+\sigma_C)
 +\Delta_d^{(\sigma)}+L_m(m-d-1).}                  \tag{4.12}
\]

An open delay-\(d\) safe path with \(v\) owner states costs at most
\(v+d\) factor letters.  Thus \(p\) open paths and \(z\) fully collared
cycles have charged total collar at most

\[
                              dp+2dz.                \tag{4.13}
\]

#### Proof

After the cut, use the linear state row consisting of all \(|C|\) states
followed by the first \(\sigma_C\) states.  The finite delay atoms are the
intersections of the preceding at most \(d+1\) states, truncated at the
two path boundaries.  The same coordinatewise positive-run proof as
Lemma 2.1 yields a factor word with the row length plus \(d\) atoms, giving
(4.10).

A cyclic depth-\(q\) window crosses the cut in one of \(q\) possible
ways, according as it needs \(1,\ldots,q\) copied prefix states.  Exactly
the first \(\sigma_C\) are retained, proving (4.11).  Summing the block
lengths, appending the omitted middle owners, the actual remaining holes,
and the tail proves (4.12).  The path assertion is the case with no
cyclic wrap; (4.13) follows by summation. \(\square\)

For a bare cut \(\sigma_C=0\), the support-blind two-sign occurrence loss
through all positive depths is exactly

\[
                         2\sum_{q=1}^{d}q=d(d+1).    \tag{4.14}
\]

Consequently \(b\) uncertified cuts are harmless from raw occurrence
counting when \(b=o(W_m/d^2)\).  If the actual post-cut target holes are
measured directly and already total \(o(W_m)\), only the path collar
remains, and the sharp count condition relaxes to
\(db=o(W_m)\), equivalently \(b=o(W_m/d)\).

## 5. A self-contained factor-blind two-tail word

For integers `a>=0`, set

\[
 A_m(a)=\binom ma-\binom m{a-1},
\tag{5.1}
\]

where a binomial with lower index `-1` is zero, and put

\[
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0.
 \end{cases}
\tag{5.2}
\]

Also define

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0,
 \end{cases}
\tag{5.3}
\]

and

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).}
\tag{5.4}
\]

### Lemma 5.1 (exact product-SCD tail)

There is a literal word of length `L_m(r)` on a `2m`-set covering every
nonempty set `S` with

\[
                         |S|\le r
 \quad\text{or}\quad
                         |S|\ge2m-r.
\tag{5.5}
\]

#### Proof

Split the ground set into two `m`-sets and fix a symmetric-chain
decomposition on each half.  A chain of minimum rank `a` has

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}.
\tag{5.6}
\]

Its forward nonempty increment word has length `w_m(a)` and realizes every
chain member as a prefix union; its reversal realizes every member as a
suffix union.  There are exactly `A_m(a)` such chains.

For every ordered pair of half-chains with minimum ranks `a,b` satisfying
`a+b<=r`, concatenate the reversed increment word of the first with the
forward increment word of the second.  If `S=S_1 union S_2` has size at
most `r`, its two containing chains obey `a+b<=|S|<=r`.  If `|S|>=2m-r`,
symmetry gives `a+b<=2m-|S|<=r`.  A suffix from the first word followed by
a prefix from the second is therefore a contiguous witness for `S`.

The total length is

\[
 \sum_{a+b\le r}A_m(a)A_m(b)(w_m(a)+w_m(b)).
\tag{5.7}
\]

The two summands are equal after swapping `a,b`, and the telescoping
identity

\[
 \sum_{b=0}^{\min(t,\lfloor m/2\rfloor)}A_m(b)=C_m(t)
\tag{5.8}
\]

turns (5.7) into (5.4). \(\square\)

### Lemma 5.2 (uniform tail estimate)

There is an absolute constant `C` such that, for `0<=d<=m-1`,

\[
 \boxed{
 {L_m(m-d-1)\over\binom{2m}{m}}
 \le C\exp\!\left(-{d^2\over8m}\right).}
\tag{5.9}
\]

#### Proof

Write `h=floor(m/2)`, `epsilon=m-2h`, `x=h-a`, and
`D_(m,x)=A_m(h-x)w_m(h-x)`.  Direct subtraction gives, for `x<h`,

\[
 D_{m,x}=\binom m{h-x}
 { (2x+\epsilon+1)^2\over h+x+\epsilon+1},
\tag{5.10}
\]

while `D_(m,h)=m`.  Formula (5.4) becomes

\[
 L_m(m-d-1)=2\sum_{x=0}^{h}D_{m,x}
 \binom m{h-(d+1-\epsilon-x)_+}.
\tag{5.11}
\]

The elementary central-binomial ratio bound

\[
 {\binom m{h-y}\over\binom mh}\le e^{-y^2/m}
\tag{5.12}
\]

follows by writing the ratio as a product and using
`log(1-t)<=-t`.  Equations (5.10)--(5.12) give

\[
 {D_{m,x}\over\binom mh}
 \le {8(x+1)^2\over m}e^{-x^2/m}
 \qquad(x<h).
\tag{5.13}
\]

Split (5.11) at `x=floor((d+1-epsilon)/2)`.  Below the split, the second
binomial in (5.11) gains `exp(-d^2/(4m))`.  Above the split, (5.13) gains
`exp(-d^2/(8m))`, leaving a Gaussian sum

\[
 {1\over m}\sum_{x\ge0}(x+1)^2e^{-x^2/(2m)}=O(\sqrt m).
\tag{5.14}
\]

Finally the standard central product estimates

\[
 {2^m\binom mh\over\binom{2m}m}=O(1),
 \qquad
 {\binom mh^2\sqrt m\over\binom{2m}m}=O(1)
\tag{5.15}
\]

absorb the two parts; the exceptional `x=h` term is exponentially small.
The below-split summation also uses the exact SCD census

\[
                 \sum_{a=0}^{\lfloor m/2\rfloor}
                    A_m(a)w_m(a)=2^m-1,             \tag{5.16}
\]

because the increment words of all symmetric chains enumerate every
nonempty subset of one \(m\)-cube exactly once.  Enlarging one absolute
constant handles bounded \(m\) and proves (5.9).
\(\square\)

The tail word is completely independent of the owner rows.  Every witness
lies within one product-chain gadget.  Consequently concatenating the tail
after the central word creates no required seam witness and costs no seam
repair.

## 6. The even constant-one theorem and Johnson specialization

### Theorem 6.1 (arbitrary cyclic-owner compiler)

Under the hypotheses and notation of Theorem 4.1, inequality (0.3) holds.

#### Proof

Theorem 4.1 covers ranks `[m-d,m+d]`.  Lemma 5.1 with
`r=m-d-1` covers its complement.  Concatenation preserves all witnesses
internal to each block, so their lengths add and give (0.3). \(\square\)

### Corollary 6.2 (constant one)

Conditions (0.4) imply (0.5).

#### Proof

The collar and hole terms in (0.3) are `o(W_m)`.  Lemma 5.2 makes the tail
`o(W_m)`.  The standard middle-antichain witness-endpoint injection,
together with Sperner's theorem, gives the matching lower bound
`nu(2m)>=W_m`. \(\square\)

### Corollary 6.3 (ordinary `H`-safe Johnson rows)

Suppose the retained rows are cyclic Johnson walks satisfying `G_H`.
Apply Theorem 6.1 with `d=H-1`.  Then (0.7) holds.  Hence

\[
 {H\over\sqrt m}\to\infty,
 \qquad H=o(m),
 \qquad K=o(W_m/H),
 \qquad
 \sum_{q=1}^{H-1}(M_q^-+M_q^+)=o(W_m)
\tag{6.1}
\]

imply coefficient one.

If every retained row has length at least `c m`, the component hypothesis
in (6.1) is automatic from `H=o(m)`:

\[
                         2(H-1)K
 \le {2H\over c m}W_m=o(W_m).
\tag{6.2}
\]

This is the promised answer for `Theta(m)` owner cycles.  There is no
hidden requirement that a component have exactly `2m`, `2m+1`, or any
other prescribed length.

## 7. Odd parity: exact lift and direct odd rows

### Lemma 7.1 (trimmed one-bit lift)

Let `Q=(Q_1,...,Q_N)` be a nonempty literal word on `V`.  For a new
coordinate `z`, the word

\[
 Q_1,\ldots,Q_N,\{z\},
 Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}
\tag{7.1}
\]

has exactly `2N` letters and covers every old target and every target
obtained by adjoining `z`.

#### Proof

Old witnesses stay in the first copy and `{z}` is explicit.  If
`Q_i,...,Q_j` witnesses a nonempty `S` and `j<N`, the corresponding
interval in the transformed copy witnesses `S union {z}`.  If `j=N`, the
interval

\[
                         Q_i,\ldots,Q_N,\{z\}
\tag{7.2}
\]

does so.  This is why the final transformed letter may be omitted. \(\square\)

Consequently

\[
                         \nu(2m+1)\le2\nu(2m).
\tag{7.3}
\]

Since

\[
 2\binom{2m}{m}
 =\left(1+{1\over2m+1}\right)\binom{2m+1}{m},
\tag{7.4}
\]

coefficient one in even dimensions implies coefficient one in odd
dimensions.  This parity transfer introduces no central collar and no
unaccounted seam: (7.2) is the only lift-internal seam witness, and its
length has already been included in the exact factor `2`.

For completeness, arbitrary owner cycles can also be compiled directly on
a `(2m+1)`-set.  Let the rows consist of `m`-sets and define

\[
 L_{i,q}=\bigcap_{t=0}^{q}X_{i+t},
 \qquad
 U_{i,q}^{\rm odd}=\bigcup_{t=0}^{q+1}X_{i+t}.
\tag{7.5}
\]

Under `G_(d+1)+P_d`, these have ranks `m-q` and `m+1+q`.  Lemma 2.1 gives

\[
 L_{i,q}=\bigcup_{j=i+q}^{i+d}B_j,
 \qquad
 U_{i,q}^{\rm odd}=\bigcup_{j=i}^{i+d+q+1}B_j.
\tag{7.6}
\]

Thus one direct odd row emits

\[
 B_0,\ldots,B_{\ell-1},B_0,\ldots,B_{2d},
\tag{7.7}
\]

of length at most `ell+2d+1`.  The extra one, compared with (3.2), is
forced by the upper depth-`d` witness, which uses `2d+2` atoms.

Let `W_m^o=binom(2m+1,m)`, let `u=W_m^o-G`, and define actual holes
`M_q^-` for rank `m-q` and `M_q^+` for rank `m+1+q`, now including the
upper-middle value `M_0^+`.  The same proof gives the direct exact bound

\[
 \boxed{
 \begin{aligned}
 \nu(2m+1)\le{}&W_m^o+(2d+1)K+M_0^+\\
 &+\sum_{q=1}^{d}(M_q^-+M_q^+)
 +2L_m(m-d-1).
 \end{aligned}}
\tag{7.8}
\]

The odd tail has length `2L_m`: apply Lemma 7.1 to the even product-SCD
tail.  It covers ranks at most `m-d-1` and at least `m+d+2`, exactly the
complement of the direct central band in (7.5).

Equation (7.8) is completely wreath-free.  It also displays the precise
direct-odd missing interface.  For a general Johnson factor there is no
reason for `M_q^+` to equal `M_q^-`.  An odd-graph double cover has a
separate opposite-parity complement identity and may reduce the two terms
to one; absent such a theorem, dropping `M_0^+` or any positive-depth
upper holes is invalid.

## 8. Decisive interface audit

The proof above uses exactly the following data from an upstream
construction.

1. **Literal states.**  Each row entry is an actual middle subset of one
   common ground set.  An abstract incidence-cycle label is insufficient.
2. **Owner disjointness.**  Retained middle owners occur at most once if
   one wants the exact baseline cancellation in (4.6).  Multiplicity must
   otherwise be charged explicitly.
3. **Delay.**  The positive coordinate runs satisfy `P_d`; ordinary
   Johnson `G_H` supplies only `P_(H-1)`.
4. **Rank correctness.**  The consecutive intersections and unions have
   the displayed ranks.  Johnson geodesicity is a convenient sufficient
   condition.
5. **Actual support.**  The aggregate lower and upper image holes, not
   merely the number of rank-correct occurrence slots, are `o(W)`.
6. **Few components.**  The copied-prefix collar is `2dK` in even
   dimension and `2d+1` per row in the direct odd construction.

Nothing else enters.  In particular the proof never invokes:

* a cyclic order of all ground coordinates;
* component length equal to the ground-set size;
* an odd-graph predecessor or successor;
* a wreath factor or a Dyck/Chung--Feller index;
* an omitted-label permutation;
* exact upper/lower complement symmetry; or
* any additional statement labelled `(B)` in an upstream reduction.

The strongest correct conclusion is therefore:

> **No wreath conversion is missing.**  Actual owner-disjoint cyclic
> Johnson rows of length `Theta(m)`, with `sqrt(m)<<H<<m`, cyclic
> `H`-geodesicity, aggregate two-sided shadow holes `o(W)`, and the safe
> depth retreat `d=H-1`, imply the sharp constant-one theorem directly.
> Their full seam toll is `2(H-1)K=o(W)`.

The sharp failure boundary is equally precise:

> **Safety alone is not enough.**  It makes every displayed trace legal
> and rank-correct but does not stop distant starts or different rows from
> colliding on the same target.  If the upstream result lacks the actual
> two-sided `o(W)` hole estimate (and, in the direct odd setting, lacks the
> upper-middle estimate `M_0^+=o(W)`), the constant-one implication remains
> unproved.  That is a target-coverage gap, not a wreath-length gap.

## 9. Self-audit of constants and boundary cases

1. At `d=0`, (3.1) is just the base owner row, with collar zero.  The
   even central band consists only of rank `m`, as it should.
2. At `d=0`, the direct odd word (7.7) copies exactly `B_0`; this is needed
   to linearize the last adjacent union and gives collar one.
3. Even upper depth `d` uses atom indices `[i,i+2d]`, hence `2d+1`
   atoms and exactly `2d` copied prefix letters.
4. Direct odd upper depth `d` uses `[i,i+2d+1]`, hence `2d+2` atoms and
   exactly `2d+1` copied prefix letters.
5. The even exterior begins at ranks `m-d-1` and `m+d+1`; therefore the
   tail parameter is exactly `r=m-d-1`.
6. The direct odd exterior begins at ranks `m-d-1` and `m+d+2`; the
   trimmed tail with the same parameter covers exactly those ranges.
7. The owner leave is charged once: `G` base atoms plus `W-G` literal
   middle repairs equals `W`, not `W+(W-G)`.
8. Concatenation uses only witnesses internal to displayed blocks.
   Therefore there is no unlisted seam term, and accidental cross-seam
   witnesses can only improve coverage.
9. Empty atoms can be deleted because every protected target has positive
   size (`d<m`), so each certified atom interval retains at least one
   nonempty letter.
10. The passage `G_H -> d=H-1` is necessary in general.  A positive run
    of exactly `H` states is compatible with `G_H` but violates `P_H`.

This completes the literal interface independently of every wreath-specific
statement.  The only surviving mathematical gate is construction of the
safe owner cycles with the displayed actual target support.

## 10. Application to the current linear-scale mixer

The current diverse-order mixer on \(Q_{2m}\) supplies an owner-disjoint
partial family with

\[
 {m\over128}<R\le {m\over64},\qquad
 \ell_C=2R,\qquad
 K={G\over2R}< {64W_m\over m},                       \tag{10.1}
\]

and \(W_m-G=o(W_m/H)\).  Its component direction word is a doubled
permutation, so every block of at most \(R\) transitions is
repetition-free.  Distinct packet directions use disjoint split pairs.
Since the construction assumes \(H\le R/4-1\), every block of \(H+1\)
transitions changes each physical coordinate at most once.  Thus the
current rows satisfy the full \(G_H+P_H\) input; no one-depth retreat is
needed for this particular construction.

The exact full collar is

\[
 2HK={HG\over R}
 <128\,{H\over m}W_m.                                \tag{10.2}
\]

Complement equivariance gives \(M_q^+=M_q^-\), so (0.3) specializes to

\[
 \nu(2m)\le
 W_m+128{H\over m}W_m
 +2\sum_{q=1}^{H}M_q^-
 +L_m(m-H-1).                                       \tag{10.3}
\]

For example, with

\[
                         H=\left\lceil\sqrt{m\log m}\right\rceil,
\tag{10.4}
\]

the collar is \(O(W_m\sqrt{\log m/m})\), while (5.9) makes the tail
\(O(W_m m^{-1/8})\).  Therefore the mixer's exact residual condition

\[
                         \sum_{q=1}^{H}M_q^-=o(W_m)  \tag{10.5}
\]

is literally the entire remaining input to coefficient one.  In the
mixer's notation this is condition (9.5c), the fused cross-cell collision
gate.  Indeed, for all sufficiently large \(m\),

\[
 W_m-G\le e^{-m/16}W_m
 <{W_m\over m+1}=W_m-N_1\le W_m-N_q
\]

for every \(q\ge1\).  Hence \(G>N_q\), so the baseline term
\((N_q-G)_+\) in the mixer's identity (9.5b) is zero and (9.5c) is
exactly (10.5).

No completion of the partial packet mosaic to a shortest odd-wreath
factor, or even to a larger exact middle factor, is used: Theorem 4.1
accepts the partial owner-disjoint family directly, and the omitted middle
owners cancel in the baseline.  The exact-wreath clause belongs to the
alternative MWB route.  It is not a premise of the direct physical-hole
route proved here.
