# A complement-antipodal Middle Levels reduction for `k=15`

Date: 2026-07-28

Status: conditional pure-math reduction.  The turn-map and cut theorems are
proved.  Existence of the decorated Hamilton cycle is open.

## 0. Main point

For every odd `k`, the Middle Levels theorem already supplies the optimal
immediate lower palette: cut a Hamilton cycle at one lower vertex.  At
`k=15` there is an additional exceptional symmetry.  Because the middle
width `W=binom(15,8)=6435` is odd, complementation can act as the half-turn
of the `2W`-cycle.  Under that action, the upper union-turn map and the next
lower intersection-turn map are literal complements.

Consequently a single surjective turn map on a complement-antipodal cycle,
followed by one well-chosen cut, gives simultaneously

\[
 (h_1,c_1)=(1,0),\qquad h_2\le2,
\]

and complete immediate upper coverage.  The independently proved scalar
compiler corridor is `h_1<=2,h_2<=5`.  Thus this one object clears both tight
pre-Hall gates at once.

## 1. The two turn maps

Let `k=2r-1` and write a Hamilton cycle of the Middle Levels incidence graph
as

\[
 T_0,X_0,T_1,X_1,\ldots,T_{W-1},X_{W-1},
\tag{1.1}
\]

cyclically, where

\[
 T_i\in\binom{[k]}r,\qquad
 X_i\in\binom{[k]}{r-1},\qquad
 X_i=T_i\cap T_{i+1}.
\tag{1.2}
\]

Define

\[
 \sigma(X_i)=T_i\cup T_{i+1}\in\binom{[k]}{r+1},
\tag{1.3}
\]

\[
 \delta(T_i)=X_{i-1}\cap X_i\in\binom{[k]}{r-2}.
\tag{1.4}
\]

These have the expected ranks because the two neighbours of a vertex in the
cycle are distinct codimension-one subsets or supersets.

The map `sigma` is exactly the immediate upper colour of the rank-`r`
projection.  The map `delta` is exactly the depth-two lower colour:

\[
 T_{i-1}\cap T_i\cap T_{i+1}=X_{i-1}\cap X_i.
\tag{1.5}
\]

Thus the first genuinely new lower gate after the Middle Levels theorem is
surjectivity of `delta`, while the first upper gate is surjectivity of
`sigma`.

## 2. Complementation identifies the gates

Assume set complementation preserves the cycle (1.1) and acts on it as the
half-turn.  Necessarily `W` is odd.  Put `s=(W-1)/2`.  After choosing the
cyclic orientation,

\[
 \overline{T_i}=X_{i+s},\qquad
 \overline{X_i}=T_{i+s+1}.
\tag{2.1}
\]

### Theorem 2.1 (turn-map duality)

For every `i`,

\[
 \boxed{\overline{\sigma(X_i)}=\delta(T_{i+s+1}).}
\tag{2.2}
\]

Consequently `sigma` is surjective if and only if `delta` is surjective, and
their complete load distributions are carried into one another by
complementation and a cyclic shift.

#### Proof

Using (2.1),

\[
 \overline{\sigma(X_i)}
 =\overline{T_i\cup T_{i+1}}
 =\overline{T_i}\cap\overline{T_{i+1}}
 =X_{i+s}\cap X_{i+s+1}
 =\delta(T_{i+s+1}).
\]

Complementation bijects the two target layers, proving the rest. \(\square\)

The same calculation holds at every depth.  If

\[
 L_i^{(q)}=\bigcap_{j=0}^{q}T_{i+j},\qquad
 U_i^{(q)}=\bigcup_{j=0}^{q}T_{i+j},
\]

then

\[
 \boxed{\overline{U_i^{(q)}}=L_{i+s}^{(q+1)}.}
\tag{2.3}
\]

Indeed the complements of the `q+1` upper vertices are `q+1` consecutive
`X` vertices, whose intersection is the intersection of the corresponding
`q+2` consecutive `T` vertices.  Therefore upper depth `q` is complete if
and only if lower depth `q+1` is complete.

### Remark 2.2 (why this does not contradict the earlier shore no-go)

An earlier complement audit projected the same alternating Middle Levels
cycle to the **lower** shore, of rank `r-1`.  On that projection,
complementation sends a lower intersection colour to an upper colour of the
opposite shore, one rank beyond the already-perfect immediate unions; it
does not make the lower projection doubly rainbow.  That conclusion remains
correct.

The OR problem in odd dimension uses `r=ceil(k/2)`, hence the **upper** shore
`T`.  On this projection the opposite-shore vertices are already the first
lower trace `X`, and De Morgan therefore gives the shifted-depth identity
(2.3).  The useful duality is thus not a reversal of the old result but a
change to the problem's correct middle shore.

### Theorem 2.3 (the undecorated antipodal carrier already exists)

Put `m=r-1`, so `k=2m+1`, and assume `m>=3` and `W` is odd.  A Hamilton
cycle

\[
 A_0,A_1,\ldots,A_{W-1},A_0
 \tag{2.4}
\]

in the odd graph `KG(2m+1,m)` lifts to a complement-half-turn invariant
Hamilton cycle of the Middle Levels graph.  Such an odd-graph Hamilton
cycle exists by the theorem of Mütze--Nummenpalo--Walczak.  Hence at
`k=15` the *undecorated* antipodal Middle Levels carrier is unconditional;
only the simultaneous turn-map, residence, and deeper-trace conditions are
open.

More explicitly, index (2.4) modulo the odd number `W` and put

\[
 X_i=A_{2i},\qquad T_i=\overline{A_{2i-1}}.
 \tag{2.5}
\]

Then `X_i=T_i cap T_(i+1)`, and if

\[
 C_j=A_{j-1}\cap A_{j+1},
 \tag{2.6}
\]

then

\[
 \boxed{\overline{\sigma(X_i)}=C_{2i},\qquad
        \delta(T_i)=C_{2i-1}.}
 \tag{2.7}
\]

Since multiplication by two permutes `Z_W`, the two turn maps have the same
load distribution for the transparent quotient reason that both are just
the length-two intersection word `(C_j)`.  Thus the decorated carrier
problem can be stated on one odd-graph Hamilton cycle:

> choose (2.4) so that its second-neighbour intersections `C_j` cover every
> `(m-1)`-set and the complementary step-two Johnson projection in (2.5)
> has depth-`d` residence (together with the deeper owner conditions).

#### Proof

Consecutive `A_j` are disjoint.  The standard bipartite double-cover lift
therefore alternates a rank-`m` set with the complement of its odd-graph
neighbour.  Because `W` is odd, the lift is one `2W`-cycle rather than two
cycles, and its second half is the complement of its first.  For (2.5), the
two sets `A_(2i-1)` and `A_(2i+1)` are distinct `m`-subsets of the
`(m+1)`-set `overline{A_(2i)}`.  Their union is that whole set, so
`T_i cap T_(i+1)=A_(2i)=X_i`.  Taking the union of the two complements gives
the first identity in (2.7); the second is immediate from the definition of
`delta`.  The Hamiltonicity input is the published odd-graph theorem.
\(\square\)

### Corollary 2.4 (turn-colouring and finite-memory residence)

Colour an edge `A_j A_(j+1)` of the odd graph by the unique element

\[
 z_j\in[k]\setminus(A_j\cup A_{j+1}).
 \tag{2.8}
\]

Then

\[
 A_{j+1}=\overline{A_j}\setminus\{z_j\},\qquad
 A_{j+2}=A_j-\{z_{j+1}\}+\{z_j\},
 \tag{2.9}
\]

and the turn at `A_j` has colour

\[
 C_j=A_j^c\setminus\{z_{j-1},z_j\}.
 \tag{2.10}
\]

Thus `sigma` (equivalently `delta`) is surjective exactly when the Hamilton
turns `(C_j)` cover every `(m-1)`-set.  Moreover the lifted upper chronology
obeys

\[
 T_{i+1}=T_i-\{z_{2i-1}\}+\{z_{2i}\}.
 \tag{2.11}
\]

It has cyclic depth-`d` residence exactly when

\[
 \boxed{z_{2i}\ne z_{2i+2t-1}
        \quad(i\in\mathbb Z_W,\ 1\le t\le d).}
 \tag{2.12}
\]

The case `t=1` is automatic for a simple Hamilton cycle, because equality
would give `A_(2i)=A_(2i+2)`.  At `k=15,d=3`, residence therefore adds only
the two nontrivial odd-offset exclusions `3` and `5`.  Since `i -> 2i`
permutes `Z_W`, (2.12) is equivalently the translation-invariant condition

\[
 z_j\ne z_{j+s}
 \quad\text{for every odd }s\in\{1,3,\ldots,2d-1\}.
 \tag{2.13}
\]

This is the smallest purely graph-theoretic carrier target obtained here:
a Hamilton cycle of `O_7` with surjective turn-colouring by the 6-sets and
two finite-memory exclusions in its edge-colour word.  All Middle Levels
and complement bookkeeping has disappeared.

#### Proof

The first identity in (2.9) is the definition of `z_j`; complement it and
apply the same identity at the next edge to get the second.  The two
neighbours of `A_j` are `A_j^c` with `z_(j-1)` and `z_j` respectively
removed, proving (2.10).  Formula (2.11) is the complement of (2.9) with
`j=2i-1`.  Finally, a coordinate inserted at transition `i` is `z_(2i)`
and the coordinate deleted `t` transitions later is `z_(2i+2t-1)`.
Avoiding equality for `1<=t<=d` is exactly cyclic depth-`d` residence.
\(\square\)

### Corollary 2.5 (Catalan regularity is forced in the quotient)

For every Hamilton cycle of `O_m`, not only a specially balanced one, each
symbol occurs exactly

\[
 C_m=\frac1{m+1}\binom{2m}{m}
 \tag{2.14}
\]

times in the edge-colour word `(z_j)`.  Consequently every coordinate has
exactly `C_m` cyclic runs in the lifted middle chronology `T`.

The turn-colour multiset `(C_j)` also has a forced point degree:

\[
 \deg_C(x)=\binom{2m}{m}-2C_m.
 \tag{2.15}
\]

If the turn colours cover every `(m-1)`-set, their excess multidesign is
therefore regular of degree

\[
 \boxed{\binom{2m}{m}-2C_m-\binom{2m}{m-2}
       =\frac{2(m-1)}{m+2}C_m.}
 \tag{2.16}
\]

At `m=7` this degree is `572`, exactly the constant appearing in the
measured `k=15` depth-two defect law.  Thus the Catalan run count and the
regular point marginals are theorems, not useful search objectives.  The
free data are the run-length distribution and the support/multiplicity
shape of the turn colours.

#### Proof

Exactly `I=binom(2m,m-1)` odd-graph vertices contain a fixed symbol `x`.
Adjacent vertices are disjoint, so the cyclic `x`-indicator has no `11`
edge.  The colour `z_j` equals `x` exactly on a `00` edge.  Hence its number
of occurrences is

\[
 W-2I=\binom{2m+1}{m}-2\binom{2m}{m-1}=C_m.
\]

Because multiplication by two permutes `Z_W`, the insertion word
`(z_(2i))` has the same histogram, proving the run statement.  There are
`W-I=binom(2m,m)` centres `A_j` avoiding `x`.  Of these, exactly `2C_m`
have `x` as one of their two incident edge colours; the two cases cannot
coincide in a simple Hamilton cycle.  This proves (2.15).  Subtracting the
point degree `binom(2m,m-2)` of the complete `(m-1)`-layer and simplifying
gives (2.16).  \(\square\)

### Theorem 2.6 (all upper ranks are one odd-graph flag cover)

Put `B_i=A_(2i)`.  For `q>=1`, define

\[
 F_i^{(q)}=\bigcap_{h=0}^{q-1}B_{i+h}.
 \tag{2.17}
\]

Then

\[
 \boxed{F_i^{(q)}
 =B_i\setminus\{z_{2i+1},z_{2i+3},\ldots,z_{2i+2q-3}\}.}
 \tag{2.18}
\]

As multisets, the complements of the upper depth-`q-1` traces of `T` are
exactly the sets `(F_i^(q))`.  Consequently the lifted middle chronology is
upper-universal at every rank if and only if, for every `1<=q<=m+1`,

\[
 \boxed{\{F_i^{(q)}:i\in\mathbb Z_W\}
        \supseteq\binom{[2m+1]}{m-q+1}.}
 \tag{2.19}
\]

Thus the turn-surjectivity condition is only the first nontrivial row
`q=2` of one full flag-cover problem.  Each start `i` supplies a descending
chain

\[
 B_i=F_i^{(1)}\supseteq F_i^{(2)}\supseteq\cdots,
 \tag{2.20}
\]

with strict descent precisely while the successive odd-indexed edge colours
are new elements of `B_i`.  If the first `m` such deletions enumerate `B_i`,
(2.20) is a maximal flag from `B_i` to the empty set.  The classical SCD
picture and the present odd-graph construction therefore meet at an exact
statement: the open upper problem is to bundle `W` lower-ideal flags into
one odd-graph Hamilton cycle.

#### Proof

Equation (2.9) with even starting index gives

\[
 B_{i+1}=B_i-\{z_{2i+1}\}+\{z_{2i}\}.
\]

An element of the initial `B_i` survives the intersection of the first `q`
vertices exactly when it is never deleted during the intervening `q-1`
transitions.  Subtracting the displayed deletion labels proves (2.18), even
when a label repeats or was not in the initial set.  The first-shadow
identity gives

\[
 L_T^{(q)}(i)=\bigcap_{h=0}^{q-1}X_{i+h}=F_i^{(q)}.
\]

The complement-half-turn identity (2.3) says that the complement of every
upper depth-`q-1` trace is a cyclic shift of this lower depth-`q` trace.
Complementation bijects the two target layers, proving (2.19).  The remaining
statements are immediate from (2.18).  \(\square\)

## 3. One cut enters the necessary prefix corridor

Delete one lower vertex, say `X_(W-1)`, from the alternating Hamilton cycle.
The remaining path is

\[
 T_0,X_0,T_1,\ldots,X_{W-2},T_{W-1}.
\tag{3.1}
\]

Project it to the rank-`r` path `T_0,...,T_(W-1)`.

### Theorem 3.1 (cut ledger)

The projected path has the following properties.

1. Its immediate lower word is `X_0,...,X_(W-2)`, hence it is simple and
   omits exactly one rank-`(r-1)` target:
   \[
   (h_1,c_1)=(1,0).
   \]
2. If the cyclic `delta` map is surjective, the path has at most two
   depth-two lower holes:
   \[
   h_2\le2.
   \]
3. If `sigma(X_(W-1))` has another preimage, immediate upper coverage
   remains complete after the cut.
4. If the cyclic rank-`r` projection has minimum cyclic coordinate-run
   length at least `d+1`, the linear projection is depth-`d` resident.

#### Proof

Part 1 is immediate from (3.1).  The full cycle has one `delta(T_i)`
occurrence at each upper vertex.  The path's depth-two lower word retains
exactly

\[
 \delta(T_1),\ldots,\delta(T_{W-2});
\]

only the two turns incident with the removed lower vertex disappear.  A
surjective cyclic image can therefore lose at most two distinct targets,
proving part 2.  The path's upper colours are all `sigma(X_i)` except the
removed occurrence, proving part 3.  Cutting a cyclic word cannot shorten an
internal run; it merely turns at most two cyclic runs into boundary runs,
proving part 4. \(\square\)

Since

\[
 W>\binom{k}{r+1},
\]

every surjective `sigma` has a repeated value.  Therefore one may always
choose the cut vertex from a non-singleton fibre.  Combining Theorems 2.1
and 3.1 gives the promised single-gate statement.

### Corollary 3.2 (single-turn-map carrier theorem)

Suppose a complement-antipodal Middle Levels Hamilton cycle has

1. a surjective turn map `sigma`; and
2. a cyclically depth-`d` resident rank-`r` projection.

Cut any lower vertex in a repeated `sigma` fibre.  The resulting middle path
is depth-`d` resident, has complete immediate upper coverage, and satisfies

\[
 (h_1,c_1)=(1,0),\qquad h_2\le2.
\tag{3.2}
\]

In particular it lies inside the necessary scalar prefix corridor
`h_1<=2,h_2<=5` required by a flat optimal compiler.

## 4. Why `k=15` is the exceptional first open case

For `k=2r-1`, Lucas' theorem gives

\[
 \binom{2r-1}{r}\equiv1\pmod2
 \quad\Longleftrightarrow\quad r\text{ is a power of two}.
\tag{4.1}
\]

Together with Theorem 2.3 and odd-graph Hamiltonicity, this is an existence
classification for the undecorated symmetry (apart from the trivial small
case): a plain-complement-invariant Middle Levels Hamilton cycle exists
precisely for

\[
 k=2^a-1.
\]

The first open dimension is exactly `k=15`, with

\[
 r=8,\quad W=6435,
 \quad\binom{15}{9}=\binom{15}{6}=5005.
\]

A surjective turn map has 1,430 units of excess, so a repeated cut fibre is
abundant.  The difficult conjunction is no longer bare symmetry or two
unrelated rainbow maps.  In the quotient language it is:

> a Hamilton cycle of `O_7` whose second-neighbour intersections cover every
> 6-set and whose missing-element edge colours avoid equality at cyclic
> distances three and five.

This is a substantially smaller mathematical object than the original
Hall-29 repair problem.

## 5. What this does not yet prove

Corollary 3.2 clears the two tight scalar lower-prefix gates and immediate
upper coverage.  An optimal OR word still requires:

1. higher upper depths, equivalently by (2.3) the deeper lower trace tower;
2. the labelled spill/containment matching for the few near-middle holes;
3. the deep lower-ideal owner assignment; and
4. the pointwise private-hit/meet conditions preserving the middle row.

The Catalan-liquidity theorem shows that after depth two the scalar reserve
jumps to `C_r+3`, so item 1 is no longer tight in mere cardinality.  The live
compiler issue is labelled compatibility, not raw capacity.

The conditional cycle above is therefore not the full conjecture disguised.
It is the first carrier lemma whose conclusion exactly matches what the
proved compiler ledger needs, while using the special symmetry unique to the
first open dimension.
