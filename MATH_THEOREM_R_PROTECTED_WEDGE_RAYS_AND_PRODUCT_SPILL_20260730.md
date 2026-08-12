# Protected wedge rays and the exact product-spill gate

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: unconditional audit and replacement theorem. The unrestricted
rank-`(r+2)` kill-shape lemma is false in the genuine odd-middle regime.
Fixed-width all-depth completeness gives a sharp outward-ray classification
and an `O(bk)` old-upper-spill bound for `b` legally opened components.
Zero spill still requires the stated locked-ray or product-dispersion
inequality; component joining and the lower compiler remain separate.

## 1. Conventions

Let `F` be a disjoint union of directed simple cycles

\[
 C=(A_0,A_1,\ldots,A_{N-1}),\qquad
 A_i\in\binom{[k]}r,
 \tag{1.1}
\]

whose consecutive vertices are Johnson neighbours.  Indices on a cycle are
cyclic.  Write `e_i=A_iA_(i+1)`.

For an upper target `Y`, a **witness** is a directed cyclic vertex interval
of \(\ell\) distinct consecutive vertices, \(1\le\ell\le N\), whose vertex
union is `Y`; its edge span is the set of its \(\ell-1\) internal factor
edges. Multiple turns around a cycle are not intervals. On a component `C`,
let

\[
 \mathcal I_C(Y)=\{\hbox{edge spans of witnesses of }Y\},
 \qquad
 K_C(Y)=\bigcap_{I\in\mathcal I_C(Y)}I .
 \tag{1.2}
\]

A component with no witness is not a supporting component and imposes no
kernel condition.  A target is **fragile on `C`** when `K_C(Y)` is nonempty.

For `q>=1`, let `\mathcal G_{C,q}(Y)` be the directed `q`-edge witnesses of
`Y`, and put

\[
 t_{C,q}(Y)=|\mathcal G_{C,q}(Y)|.
 \tag{1.3}
\]

If `|Y|=r+q`, every member of `\mathcal G_{C,q}(Y)` is geodesic in the
following elementary sense: starting with `r` elements, each of its `q`
steps introduces one element not seen earlier in the interval.

A **wedge** at `A_i` is a pair of adjacent edges

\[
 P_i=\{e_{i-1},e_i\}
 \tag{1.4}
\]

with equal adjacent union colours,

\[
 A_{i-1}\cup A_i=A_i\cup A_{i+1}.
 \tag{1.5}
\]

Equivalently, one coordinate is absent at `A_i` and present at both
neighbours.  The two one-edge intervals in (1.4) witness the same
rank-`(r+1)` target.

The fixed-width all-depth hypothesis used below is explicit:

> **(FW)** Every rank-`(r+q)` target under discussion has at least one
> directed `q`-edge witness somewhere in the factor.

This is the relevant consequence of the audited PBBS all-depth flag tower
after applying the appropriate complement.  Arbitrary-width support alone
is weaker than (FW).

## 2. Audit of the odd-middle `J(9,5)` counterexample

Consider

\[
 12389,12489,13489,13589,15689,15789,12789.
 \tag{2.1}
\]

Here `r=5=(k+1)/2`. At `12489`, coordinate `3` gives a wedge; both
flanking unions are `123489`.
For

\[
 Y=12345689
 \tag{2.2}
\]

the vertices contained in `Y` form the single cyclic run

\[
 12389,12489,13489,13589,15689.
\]

The coordinate `6` forces the last vertex, coordinate `2` forces the first
or second vertex, and coordinate `4` then leaves exactly the two witnesses

\[
 [12389,12489,13489,13589,15689],\qquad
 [12489,13489,13589,15689].
 \tag{2.3}
\]

Their edge spans are `{0,1,2,3}` and `{1,2,3}`.  Hence

\[
 K_C(Y)=\{e_1,e_2,e_3\}.
 \tag{2.4}
\]

In particular the right wedge edge `e_1` is killed by a target of rank
`8=r+3`. This independently confirms the corrected odd-middle item 2019 and
`MATH_AUDIT_WEDGE_KILL_SHAPE_COUNTEREXAMPLE_20260730.md`.  Notice also that
the left wedge edge `e_0` is not killed by this target: the example refutes
the asserted rank shape, not the existence of a safe side at this wedge.

### Proposition 2.1 (odd-middle suspension)

For every \(r\ge5\), the same counterexample exists in
\(J(2r-1,r)\).

#### Proof

Adjoin a common set of \(r-5\) new coordinates to every displayed vertex
and to `Y`, and add a further \(r-5\) unused ambient coordinates. The vertex
rank becomes \(r\), the ambient size becomes
\(9+2(r-5)=2r-1\), and the target rank becomes
\(8+(r-5)=r+3\). Johnson adjacency, the two witnesses, and their edge
kernel are unchanged. QED.

## 3. Kernel size from fixed-width multiplicity

### Lemma 3.1 (geodesic-interval kernel bound)

Let `|Y|=r+q`, let `q<N`, and suppose `t=t_(C,q)(Y)>=1`.  Then

\[
 |K_C(Y)|\le (q+1-t)_+ .
 \tag{3.1}
\]

In particular `t>=q+1` makes the component kernel empty.

#### Proof

The full kernel is contained in the intersection of the edge spans of the
`q`-edge witnesses.  If those spans have empty intersection there is
nothing to prove.  Otherwise cut the edge circle at a common edge and
unwrap all `t` spans into integer intervals of `q` consecutive edges.  If
their distinct start positions have minimum `a` and maximum `b`, their
intersection has `q-(b-a)` edges.  The starts are distinct, so
`b-a>=t-1`.  Therefore the intersection has at most `q+1-t` edges.  QED.

The hypothesis `q<N` is harmless for the PBBS middle cycles in the usual
depth range.  Without it, the safe fallback is the literal definition
(1.2), not (3.1).

### Lemma 3.2 (weighted form)

Let `\Omega_C` be a finite bank of opening options on `C`, each option
cutting one old edge, and let `\mu_C` be a probability distribution on the
bank.  Put

\[
 \rho_C=\max_{e\in E(C)}
 \mu_C\{a\in\Omega_C:a\hbox{ cuts }e\}.
 \tag{3.2}
\]

If `t_(C,q)(Y)>=1`, then

\[
 \mu_C\{a:a\hbox{ cuts an edge of }K_C(Y)\}
 \le \rho_C(q+1-t_{C,q}(Y))_+ .
 \tag{3.3}
\]

#### Proof

Apply the union bound over the kernel edges and then Lemma 3.1.  QED.

For a uniform option bank in which at most `delta_C` options cut one edge,
one may take `rho_C<=delta_C/|Omega_C|`.

## 4. The corrected wedge theorem

For a wedge at `A_i`, define its outward `q`-edge rays

\[
 L_{i,q}=\bigcup_{j=i-q}^{i}A_j,
 \qquad
 R_{i,q}=\bigcup_{j=i}^{i+q}A_j.
 \tag{4.1}
\]

The fixed-width hypothesis in the next theorem is essential. Arbitrary
interval support does not suffice even at odd middle rank: in the
`J(9,5)` cycle

```
12589,12389,12489,13489,13689,13789,12789
```

coordinate `3` is a wedge at `12489`, while `Y=12345689` has the unique witness

```
12589,12389,12489,13489,13689.
```

Its four-edge kernel contains **both** wedge flanks.  There is no geodesic
three-edge witness of `Y`: the two possible length-four vertex intervals
near the wedge miss respectively `6` and `5`.  Hence Theorem 4.1 must not be
invoked from arbitrary-width upper completeness alone.

### Theorem 4.1 (outward-ray classification)

Fix a wedge `P_i={e_(i-1),e_i}`, a depth `q>=2` with `q<N`, and a target
`Y` of rank `r+q` having a `q`-edge witness on `C`.

1. If `e_(i-1) in K_C(Y)`, then `Y=L_(i,q)`.
2. If `e_i in K_C(Y)`, then `Y=R_(i,q)`.
3. The kernel `K_C(Y)` cannot contain both wedge edges.

Thus at each depth there is at most one possible higher-rank killer on each
side of a wedge.  Killers of rank `r+3,r+4,...` are not excluded; they are
pinned to the corresponding outward ray.

#### Proof

Let

\[
 U=A_{i-1}\cup A_i=A_i\cup A_{i+1}.
\]

Traverse the two wedge transitions from `A_(i-1)` to `A_i` to `A_(i+1)`.
The element inserted on the second transition is the unique element of
`U\setminus A_i`.  It was already present in `A_(i-1)`, because consecutive
vertices are distinct `r`-subsets of the `(r+1)`-set `U`.  Hence, in any
directed interval containing both wedge edges, one of those two transitions
introduces no new element to the running union.

A `q`-edge interval starts with `r` elements and has only `q` transitions.
If it contains both wedge edges, its union consequently has size at most
`r+q-1`; it cannot witness a rank-`(r+q)` target.

Now assume `e_(i-1) in K_C(Y)`.  Every `q`-edge witness of `Y` contains that
edge, and by the preceding paragraph it excludes `e_i`.  A directed
`q`-edge interval containing `e_(i-1)` but not its immediate successor
`e_i` must end at `A_i`; since `q<N`, it is exactly the left ray in (4.1).
Its union is `L_(i,q)=Y`.  The right statement is symmetric.  If both wedge
edges lay in the kernel, every `q`-edge witness would contain both, which
was just proved impossible.  QED.

### Corollary 4.2 (exact opposing-ray obstruction)

Assume (FW) on a one-cycle factor.  A wedge has no higher-shadow-safe flank
if and only if there are (not necessarily equal) depths `q_L,q_R>=2` such
that

\[
 e_{i-1}\in K_C(L_{i,q_L}),qquad
 e_i\in K_C(R_{i,q_R}),
 \tag{4.2}
\]

where the displayed ray unions have the indicated ranks.  No single target
can supply both obstructions.

#### Proof

Necessity is Theorem 4.1 applied separately to a killer of each flank.
Sufficiency is the definition of a killed cut edge.  QED.

This is the precise replacement for the false “every killer has rank
`r+2`” assertion.  The minimal surviving countercondition is an opposing
pair of locked outward rays, potentially at two different depths.

### Corollary 4.3 (safe-wedge dispersion count)

Assume (FW) on this one-component factor. Let `P` be a set of `omega`
wedges on the component and regard the two
flanks of each wedge as `2 omega` labelled opening options.  Let `Lambda`
be the number of triples `(wedge,side,q)`, `q>=2`, for which the outward
ray has rank `r+q` and its flank belongs to the kernel of that ray target.
Then the number of higher-shadow-safe labelled options is at least

\[
 2\omega-\Lambda.
 \tag{4.3}
\]

In particular

\[
 \Lambda<2\omega
 \tag{4.4}
\]

guarantees a safe wedge flank.

#### Proof

By Theorem 4.1 every dangerous labelled flank produces at least one of the
counted locked-ray triples.  Multiple depths can charge the same dangerous
flank, so the number of dangerous options is at most `Lambda`.  QED.

This inequality is deliberately about locked rays, not all upper targets.
It is often much smaller than a union bound over the whole Boolean upper
ideal.

### Theorem 4.4 (assigned-geodesic wedge spill)

Let `F` have `b` components and assume (FW). Assign to every
rank-`(r+q)` target one particular `q`-edge
witness and its provider component `a(Y)`.  In every component choose one
wedge and cut either one of its two flanks.  Then the number of upper targets
which lose **all old component-interior witnesses** is at most

\[
 \sum_{a=1}^b g_a\le b(k-r-1),                     \tag{4.5}
\]

where `g_a` is the number of depths `q=2,...,k-r` for which the chosen
outward `q`-ray on component `a` has the maximum possible union rank `r+q`.
Only depths `q<|C_a|` can contribute; this is automatic for any assigned
`q`-edge cyclic interval.

More precisely, for every ordered pair `(component,q)` with `q>=2`, at most
one lost target is assigned to that pair.  When `k=2r-1`, (4.5) is

\[
                         b(r-2).                    \tag{4.6}
\]

#### Proof

Fix a target `Y` which loses every old witness.  In particular, its assigned
`q`-edge witness on `C_(a(Y))` contains the chosen cut edge of that component.
The assigned interval cannot contain both flanks of the chosen wedge, by the
geodesic rank argument in Theorem 4.1.  It is consequently the unique
outward `q`-edge ray on the chosen side.  Its union, and hence `Y`, is uniquely
determined by `(a(Y),q)`.  This proves injectivity.

At `q=1`, the chosen cut edge and the opposite wedge flank are two distinct
one-edge witnesses of the same target, so no first-upper target is lost.
There are exactly `k-r-1` remaining depths `q=2,...,k-r`.  Summing one target
per eligible component and depth gives the first inequality in (4.5), and
discarding eligibility gives the second.  QED.

More constructively, for the chosen flank on `C_a` form the ray list

\[
 \mathcal R_a=
 \left\{\bigcup I_{a,q}:
 2\le q\le k-r,\ q<|C_a|,\
 \left|\bigcup I_{a,q}\right|=r+q\right\},           \tag{4.7}
\]

where \(I_{a,q}\) is its unique outward `q`-edge interval. Every old-lost
upper target belongs to \(\bigcup_a\mathcal R_a\). Appending this explicit
list blindly therefore restores the upper support using at most
\(\sum_a g_a\le b(k-r-1)\) literal nonzero cells. Consequently an already
owner-, seam-, residence-, and
compiler-compatible construction with `b=O(1)` components has upper spill
`O(k)`.  This conclusion does not assert that the component joins or the
common compiler exist; it removes the false wedge kill-shape lemma from the
upper-spill step once those independent interfaces are supplied.

If an independent condition `(E1)` already proves that the chosen flank
preserves every rank-`(r+2)` target, then the depth `q=2` term vanishes and
the same proof gives

\[
        |\mathcal L_{\ge r+3}|
        \le b\max\{k-r-2,0\}.                       \tag{4.8}
\]

Thus the exact role of `(E1)` is additive: it removes one possible ray per
component.  It does not need the false assertion that all remaining killers
also have depth two.

## 5. Exact product-wedge incidence and `(SPILL)`

Suppose components `C_1,...,C_s` have nonempty finite banks
`Omega_1,...,Omega_s` of residence-admissible one-edge openings.  A choice
`a=(a_1,...,a_s)` cuts one edge in each component.  For a target `Y`, let

\[
 S(Y)=\{j:\mathcal I_{C_j}(Y)\ne\varnothing\}
 \tag{5.1}
\]

and, for `j in S(Y)`, put

\[
 H_j(Y)=\{a_j\in\Omega_j:
          a_j\hbox{ cuts an edge in }K_{C_j}(Y)\}.
 \tag{5.2}
\]

Define the bad product box

\[
 B_Y=\prod_{j\in S(Y)}H_j(Y)
     \times\prod_{j\notin S(Y)}\Omega_j.
 \tag{5.3}
\]

Let \(\mathcal A\) be any nonempty family of **jointly admissible** opening
tuples inside \(\prod_j\Omega_j\). Individual residence legality of each
bank does not imply that the full Cartesian product is seam-, owner-, and
compiler-compatible; that stronger property must be proved before taking
\(\mathcal A=\prod_j\Omega_j\).

### Theorem 5.1 (exact admissible-atlas old-witness criterion)

There is a tuple in \(\mathcal A\) retaining at least one old interior
witness of every upper target if and only if

\[
 \mathcal A
 \not\subseteq \bigcup_{|Y|>r}B_Y.
 \tag{PWI}
\]

#### Proof

For a supporting component `C_j`, cutting `e` destroys every old witness of
`Y` on that component exactly when `e in K_(C_j)(Y)`.  All old witnesses of
`Y` are destroyed exactly when this happens on every supporting component,
which is exactly membership in `B_Y`. Avoiding the union of the bad boxes
inside the admissible atlas is therefore necessary and sufficient. QED.

`(PWI)` is exact for retaining old witnesses.  A newly inserted seam can
create a replacement witness, so `(PWI)` is sufficient but not necessary
for the unrestricted rethreaded factor.

### Theorem 5.2 (general admissible-atlas spill potential)

Give \(\mathcal A\) any probability distribution \(\pi\), and put

\[
 \Phi_{\mathcal A}(\pi)=
 \sum_{|Y|>r}\pi(\mathcal A\cap B_Y).                  \tag{5.4}
\]

Some admissible tuple loses all old witnesses of at most
\(\lfloor\Phi_{\mathcal A}(\pi)\rfloor\) upper targets. In particular,
\(\Phi_{\mathcal A}(\pi)<1\) implies `(PWI)`.

#### Proof

The summand is exactly the probability that `Y` loses all old witnesses.
Linearity of expectation and integrality give the assertion. QED.

### Corollary 5.3 (weighted Cartesian product-spill criterion)

Suppose the complete Cartesian bank is jointly admissible, take
\(\mathcal A=\prod_j\Omega_j\), and give each bank an arbitrary probability
distribution `mu_j` independently. Put

\[
 \boxed{
 \Phi:=\sum_{|Y|>r}
       \prod_{j\in S(Y)}\mu_j(H_j(Y)).
 }
 \tag{SPILL}
\]

There is a tuple losing all old witnesses of at most
\(\lfloor\Phi\rfloor\) targets. In particular, \(\Phi<1\) implies `(PWI)`.

#### Proof

Under the product measure, `Pr(B_Y)` is the displayed product. Apply
Theorem 5.2. QED.

This is valid for nonuniform/optimized banks and is stronger than counting
all killer incidences without component support information.

### Corollary 5.4 (multiplicity-certified product spill)

Assume the jointly admissible complete-Cartesian-bank hypothesis of
Corollary 5.3, and assume that every option in every `Omega_j` cuts a wedge
flank (so its paired opposite flank remains present after the one cut).
Let `Y` have rank `r+q`.  For every supporting component set

\[
 \beta_j(Y)=
 \begin{cases}
 \min\{1,\rho_j(q+1-t_{C_j,q}(Y))_+\},&t_{C_j,q}(Y)>0,\\
 1,&t_{C_j,q}(Y)=0.
 \end{cases}
 \tag{5.5}
\]

Then the checkable inequality

\[
 \sum_{q\ge2}\ \sum_{|Y|=r+q}
       \prod_{j\in S(Y)}\beta_j(Y)<1
 \tag{5.6}
\]

implies zero old-witness spill and hence `(PWI)`.

#### Proof

Lemma 3.2 bounds each factor with positive fixed-width multiplicity; the
trivial bound one is used on the other supporting components.  A q1 target
cannot kill a wedge-flank option: if its colour is the wedge colour, the
other flank is a distinct one-edge witness, and if it is not the wedge
colour, that edge is not a witness of the target at all.  Thus only `q>=2`
remains.
Multiply the component bounds and apply Corollary 5.3. QED.

For a componentwise fixed-width-complete bank this uses every supporting
component.  Under merely global (FW), at least one component has positive
`t`, while components carrying only long witnesses correctly retain the
factor one in (5.5).

### Corollary 5.5 (binary wedge-side product bound)

Assume the resulting Cartesian family of binary choices is jointly
admissible.  Fix one wedge in each component and choose its left or right
flank uniformly.
For `|Y|=r+q`, let

\[
 G(Y)=\{j\in S(Y):t_{C_j,q}(Y)>0\}.
 \tag{5.7}
\]

Then

\[
 \Pr(Y\hbox{ loses every old witness})
 \le 2^{-|G(Y)|}.                                  \tag{5.8}
\]

Consequently

\[
 \sum_{q\ge2}\sum_{|Y|=r+q}2^{-|G(Y)|}<1          \tag{5.9}
\]

is a zero-spill certificate, and the same sum without the strict bound is
an upper bound on expected literal spill.

#### Proof

On every component in `G(Y)`, Theorem 4.1 says that `K_C(Y)` contains at
most one of the two wedge flanks.  Thus the corresponding product factor is
at most `1/2`.  On the remaining supporting components use the trivial
factor one, multiply, and invoke Corollary 5.3. QED.

This is stronger than the raw kernel-size estimate for a two-option bank:
the geodesic wedge shape gives `1/2` independently of `q`, whereas
`(q+1-t)/2` becomes vacuous at larger depths.

## 6. What residence does and does not add

If every cyclic positive coordinate run has length at least `d+1`, opening
any one old edge leaves every internal run unchanged; only the run crossing
the cut is split into two boundary runs.  Hence every single-edge opening
is linearly `d`-resident.  This proves that the banks in Section 5 may be
formed from old wedge flanks without an additional one-component residence
loss.

After several components are joined, new seams can turn boundary fragments
into short internal runs.  Their exact seam collars still have to be
checked.  Residence alone does not supply a lower bound larger than one on
`t_(C,q)(Y)`.  Here is a uniform local counterexample, included to make that
scope exact.

### Proposition 6.1 (arbitrarily strong residence permits a locked ray)

For every `d>=1` there is a simple cyclic Johnson chronology whose internal
cyclic positive runs all have length at least `d+1`, and which has a wedge
flank killed by a higher-rank target having exactly one geodesic
fixed-width occurrence.

#### Proof

Start with the following cycle in `J(8,4)`:

```
1458, 1345, 2345, 1245, 1256, 1267, 1678, 1568.
```

Its cyclic positive-run lengths are at least two (coordinate by coordinate
the minimum is attained by `3` and `7`).  At `2345`, coordinate `1` gives a
wedge.  The right wedge edge is `2345--1245`.  The target

\[
                         Y=1234567
\]

has precisely the two witnesses

```
1345,2345,1245,1256,1267
2345,1245,1256,1267,
```

so the right wedge edge belongs to its kernel; the second displayed witness
is its unique three-edge geodesic occurrence.

Now replace every base coordinate `a` by a block of `h=d` clones.  Replace
each base Johnson transition, which deletes `a` and inserts `b`, by `h`
successive Johnson transitions pairing the clone deletions and insertions.
The eight base edge intersections are the distinct triples

\[
 145,345,245,125,126,167,168,158,
\]

so the interpolated cycle is simple.  A clone remains present across at
least one complete intervening `h`-step base transition because every base
positive run has at least two vertices.  Hence every expanded positive run
has at least `h+1=d+1` vertices.

At the incoming wedge transition remove a distinguished clone of coordinate
`1` last, and at the outgoing transition add it first while deleting a
distinguished clone of coordinate `3`.  The intervening block state is a
wedge for that clone.  Let `Y_h` consist of all clones of coordinates
`1,...,7`.  The transition from the central block state through the next
three base transitions is a geodesic `3h`-edge witness of `Y_h`.  Every
witness must cross the distinguished outgoing micro-edge: the distinguished
`3`-clone occurs only on its left within the `Y_h`-contained run, whereas
the clones of coordinate `7` force extension to its right.  The adjacent
base transitions involving coordinate `8` delimit that contained run.
Thus the wedge edge lies in `K(Y_h)`, and the displayed geodesic occurrence
is unique.  QED.

This proposition is not a protected all-target PBBS factor; it proves only
the claimed nonimplication from residence.  Whether the additional global
PBBS organization forces useful recurrence is exactly the dispersion gate.
In fact the same distinguished-`3` anchor shows that every geodesic prefix
of the expanded right ray of depth `q=h+1,...,3h` is a distinct target whose
kernel contains the chosen wedge edge: it still needs the distinguished
`3`-clone from the left of the cut, and it now also needs a newly introduced
`6`- or `7`-clone on the right.  The endpoint `q=h` is deliberately omitted,
because the full incoming macro transition has the same block union and
avoids the chosen flank.  Thus `2h=Theta(k)` lost ray targets are compatible
with arbitrarily strong residence and local fixed-width witnesses.  The
`O(bk)` order in Theorem 4.4 cannot be improved from those two local
properties alone.

The audited PBBS fixed-width support theorem also gives only the stated
pointwise lower bound one:

\[
 1\le \mu^{\rm corr}_{P,q}(Y)
 \le {2q+1\choose q};
 \tag{6.1}
\]

its lower bound is exactly one.  Consequently the missing all-`k` input is
a deletion-stable multiplicity/dispersion estimate, or a direct proof of
the locked-ray inequality (4.4), not another support assertion.

There is also a capacity reason not to impose two geodesic witnesses for
every higher target.  In the odd middle dimension `k=2r-1`, there are

\[
 W={2r-1\choose r}
\]

cyclic two-edge window starts but

\[
 N_2={2r-1\choose r+2}
\]

rank-`(r+2)` targets.  Universal double geodesic coverage would require
`W>=2N_2`, whereas

\[
 {W\over N_2}={(r+1)(r+2)\over(r-1)(r-2)}<2
 \qquad(r\ge9).
 \tag{6.2}
\]

Thus the blanket two-witness replacement is unavailable in the all-`k`
range. Selective outward-ray recurrence or the product dispersion in
(5.6) is the correct scale.

## 7. Exact proved boundary

The following statements are unconditional.

1. The odd-middle `J(9,5)` example invalidates the unrestricted
   rank-`(r+2)` killer claim.
2. On any component carrying a fixed-width `q`-edge witness, every
   rank-`(r+q)` killer of a wedge flank is the unique outward ray, and its
   kernel cannot contain both flanks. Global (FW) suffices for Theorem 4.4,
   but not for this assertion on every supporting component.
3. `(PWI)` is necessary and sufficient for preserving an old upper witness
   inside the declared jointly admissible opening atlas.
4. `(SPILL)`, (5.6), and the one-component locked-ray inequality (4.4) are
   rigorous sufficient conditions.
5. Under (FW), the assigned-geodesic theorem gives the protected upper spill
   bound `b(k-r-1)` for a `b`-component wedge opening.
6. Cyclic residence makes the individual old openings residence-safe, but
   does not prove any of those strict dispersion inequalities or certify the
   new seams/compiler.

Therefore the strongest currently justified protected-factor replacement is
not “all killers have rank `r+2`.”  It is the outward-ray/PWI theorem.  Zero
spill still requires either
`Lambda<2omega` for one component or `Phi<1` for the product bank, but
`b=O(1)` already gives `O(k)` upper spill by Theorem 4.4.  The lower compiler
and the seam residence ledger remain separate obligations.

## 8. Independent audit and authoritative counterexample

Only the corrected odd-middle v2 counterexample is cited:

```text
MATH_AUDIT_WEDGE_KILL_SHAPE_COUNTEREXAMPLE_20260730.md
  b3545e30ec30a185945173a8e341914284a165413215bccb83f02d9a8972a157
scratch/audit_wedge_kill_shape_counterexample_20260730.py
  def737c316aeb444cb3ef18f117731d3937d83e5551df67eaa7579353bf57598
payload
  7a69d3a2f54465694469d3a763f6ca792072764bbe2f1f4e60ec9c03430d7343
```

The script retains the legacy internal schema string
`wedge-kill-shape-counterexample-v1`. Here “v2” means the corrected
odd-middle byte version pinned by the three hashes above; the legacy schema
label is not used as provenance.

The decisive assigned-geodesic injection was independently audited with
all quantifiers and off-by-one constants. The audit also checked the two
scope boundaries which are easiest to overstate:

1. all losses in this note concern old component-interior witnesses; a new
   seam may restore them, so the bound is a safe upper bound on final loss;
2. the product formula is invoked only for a jointly admissible Cartesian
   bank, while Theorem 5.2 handles an arbitrary jointly admissible atlas.

No finite SAT, exhaustive search, or web result is used. The only remaining
hypothesis needed for the `O(bk)` upper-spill theorem is literal (FW) plus
the existence of a jointly installable wedge-flank cut on each opened
component. All-depth arbitrary-width support and residence alone are
explicitly insufficient, as Sections 4 and 6 show.
