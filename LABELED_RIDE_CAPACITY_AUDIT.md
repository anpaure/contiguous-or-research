# Independent audit of `LABELED_RIDE_CAPACITY.md`

## 1. Verdict

Most of the local mathematics in the note is correct.

* Lemma 1 gives valid uniform upper bounds on the number of slab targets for
  which one entry can achieve a prescribed coordinate set.  The bounds are
  not the exact capacities advertised by the section title.  In the regime
  `1<=h<=a`, the exact maximum for one prescribed coordinate is

  \[
  h(2a+1)-\left\lfloor\frac{h^2}{4}\right\rfloor,       \tag{1.1}
  \]

  whereas the displayed portal realizes

  \[
  h(2a+1)-\frac{h(h+1)}2.                              \tag{1.2}
  \]

  Thus the portal is sharp in order `Theta(ah)`, but not in its quadratic
  constant when `h=Theta(a)`.
* The `4a+1` portal word and all its interval joins are correct.  It is a
  standalone contiguous multiplexing example.  Only the portal entry, not
  the two complete arms, is shown to respect an arbitrary ride cap.
* The fresh-head/fresh-tail regions are correctly localized and are
  pairwise disjoint on each side.  The compatibility-graph inequality

  \[
  N\ge2Q-\nu(\Gamma),\qquad
  D\ge M-2R-\nu(\Gamma)=\Delta(\Gamma)-R               \tag{1.3}
  \]

  is a valid necessary bound.
* The A-turn example is genuinely legal and factorable.  Its maximal factor
  really shares `a-1` fresh tail labels of the first ride with `a-1` fresh
  head labels of the second ride.

The principal overstatement is the interpretation of that example.  It
proves that the **fresh middle-label position count** is not additive ride
by ride.  It does not construct witnesses for all below-middle slab targets
of the two rides and therefore does not, by itself, refute every possible
additive two-chain covering-defect theorem.  Likewise, the sentence that a
three-direction windmill can continue the matching indefinitely is a
plausible extrapolation, not something proved by the two-ride gadget.

## 2. Exact per-entry label capacities

Let

\[
 \mathcal F_h=\{U\in[0,2a]^3:3a-h\le\rho(U)\le3a-1\}
\]

and

\[
 \operatorname{Ach}_C(b)
 =\{U\in\mathcal F_h:b\le U,\ U(c)=b(c)\ (c\in C)\}.
\]

### 2.1 Audit of Lemma 1

The three displayed upper bounds

\[
 |\operatorname{Ach}_C(b)|\le
 \begin{cases}
 h(2a+1),&|C|=1,\\
 h,&|C|=2,\\
 1,&|C|=3
 \end{cases}                                           \tag{2.1}
\]

are correct.  At a fixed rank, prescribing one coordinate leaves a bounded
two-variable sum with at most `2a+1` solutions; prescribing two coordinates
leaves at most one value; prescribing all three fixes the target.

They are coarse uniform bounds, not exact maxima.  For two prescribed
coordinates the exact uniform maximum is

\[
                   \min(h,2a+1),                       \tag{2.2}
\]

because only one coordinate remains and it has `2a+1` possible values.
This maximum is attained by choosing the fixed-coordinate sum so that the
remaining coordinate traverses the intersection of the `h` slab ranks with
`[0,2a]`.  For three prescribed coordinates the exact maximum is one.

For one prescribed coordinate, define the triangular coefficient

\[
 c_a(s)=\#\{(y,z)\in[0,2a]^2:y+z=s\}
 =\begin{cases}
 2a+1-|s-2a|,&0\le s\le4a,\\
 0,&\text{otherwise}.
 \end{cases}                                           \tag{2.3}
\]

The exact uniform capacity is

\[
 K_1(a,h)=
 \max_{0\le x\le2a}\sum_{q=1}^h c_a(3a-q-x).          \tag{2.4}
\]

Indeed, positive values in the two unlabelled coordinates of `b` can only
remove targets, so the optimum has `b=(x,0,0)` after permuting coordinates.
At distance `q` below the middle, the other two coordinates must sum to
`3a-q-x`, giving (2.4).

For the range used by the portal, `1<=h<=a`, a centered block of `h`
coefficients of the triangle is feasible.  The sum of the `h` largest
consecutive coefficients is

\[
 K_1(a,h)=h(2a+1)-\left\lfloor\frac{h^2}{4}\right\rfloor. \tag{2.5}
\]

For example, if `h=2m`, take `x=a-m`; the sums have offsets
`-m,-m+1,...,m-1` from `2a`.  If `h=2m+1`, take `x=a-m-1`; the offsets are
`-m,...,m`.  Their total absolute deviations are respectively `m^2` and
`m(m+1)`, proving (2.5).

Thus the note's important qualitative conclusion—one label has quadratic
capacity when `h=Theta(a)`—is correct, but “exact capacity” and “sharp”
should be read as order-of-magnitude statements unless (2.4)/(2.5) replaces
the coarse first line of (2.1).

## 3. Audit of the `4a+1` portal

The word is

\[
 (0,2a,0),(0,2a-1,0),\ldots,(0,1,0),
 (a,0,0),
 (0,0,1),\ldots,(0,0,2a).              \tag{3.1}
\]

It has exactly `2a+1+2a=4a+1` entries.  For `y,z>0`, start at the left-arm
entry `(0,y,0)` and end at the right-arm entry `(0,0,z)`.  The included
left-arm values decrease from `y` to one, and the included right-arm values
increase from one to `z`, so the coordinatewise join is exactly

\[
                         (a,y,z).                     \tag{3.2}
\]

If `y=0`, begin at the portal; if `z=0`, end there.  Hence every pair
`0<=y,z<=2a` is represented as claimed.

In the slab rank `3a-q`, the equation is `y+z=2a-q`.  For
`1<=q<=h<=a`, this has `2a-q+1` bounded nonnegative solutions.  Therefore
the portal belongs to exactly

\[
 \sum_{q=1}^h(2a-q+1)
 =h(2a+1)-\frac{h(h+1)}2                        \tag{3.3}
\]

of these target intervals.  The count and contiguity claim are fully
correct.

At `h=a`, (3.3) is `(3/2)a^2+O(a)`, while the true one-label maximum (2.5)
is `(7/4)a^2+O(a)`.  This quantifies the sense in which the portal is not
constant-sharp.  When `h=o(a)`, both have leading term `2ah`, so it is
asymptotically sharp in that thinner regime.

The cap sentence needs one qualification.  The portal entry `(a,0,0)` is
legal at any covered position with cap `G_p>=(a,0,0)`; no cross-coordinate
cap is needed **at that one position**.  But the complete interval gadget
also uses arm entries with `y` or `z` as large as `2a`.  The note does not
show that those arm positions fit the moving caps of an arbitrary ride, nor
that many levels of such arms can coexist without contaminating one
another.  Thus (3.1) is a valid counterexample to a uniform per-entry label
capacity, not yet an embedded factorable windmill construction.

Similarly, `O(a)` portal entries have the raw potential for `Theta(a^3)`
coordinate-target incidences, but realizing all those incidences with
shared contiguous arms is exactly the unresolved contamination problem in
Section 9 of the source note.

## 4. Fresh achievements and the compatibility graph

Suppose consecutive selected middle targets `T_i,T_{i+1}` lie in one ride,
with coordinate `u_i` increasing and coordinate `d_i` decreasing.  Since
every entry of `I_i` is at most `T_i`, no entry in `I_i` can attain the new
larger value `T_{i+1}(u_i)`.  A witness for `T_{i+1}` must therefore attain
it in

\[
 \mathcal Q_i=I_{i+1}\setminus I_i
 \subseteq[r_i+1,r_{i+1}].                         \tag{4.1}
\]

The symmetric argument puts an achievement of the removed value `T_i(d_i)`
in

\[
 \mathcal H_i=I_i\setminus I_{i+1}
 \subseteq[\ell_i,\ell_{i+1}-1].                   \tag{4.2}
\]

The inclusions remain correct when consecutive selected intervals are
disjoint: the set difference then starts later than the displayed bounding
interval, which causes no problem.

The blocks `[ell_i,ell_{i+1}-1]` are pairwise disjoint, as are the blocks
`[r_i+1,r_{i+1}]`.  Hence one chosen head position per ride transition is
distinct from every other chosen head, and similarly for tails.  A physical
position can identify at most one head with at most one tail.

Every point in a head or tail difference belongs to at least one selected
middle witness.  Therefore it is covered and has the well-defined cap

\[
 G_p=\bigwedge_{j:p\in I_j}T_j.                     \tag{4.3}
\]

The free positions from Lemma G cannot satisfy these particular fresh
demands, exactly as the note states.

### 4.1 Cap compatibility

Suppose `p` lies in `H_i intersect Q_k`.  If `d_i` and `u_k` differ, an
entry can attain both requested labels exactly when each requested value is
at most the corresponding coordinate of `G_p`: put those two values in the
entry and put zero in the third coordinate.  If the requested coordinates
coincide, the two values must agree and be at most that cap coordinate.

There is no hidden zero-entry problem: a decreasing fresh value is positive,
as is an increasing fresh value.  Thus the proposed entry is nonzero.
The edge definition in `Gamma` is therefore exactly the correct
**pairwise cap-compatibility** test.

It is intentionally only a possibility graph.  Different edges may not be
simultaneously realizable once all central-window pins and below-target
witnesses are imposed.  This can only reduce actual sharing, so using
`nu(Gamma)` remains safe for a necessary lower bound.

### 4.2 Matching inequality

Let `Q=M-R` be the number of transitions internal to `R` consecutive rides.
Choose one head achievement and one tail achievement for every transition.
There are `Q` distinct head positions and `Q` distinct tail positions.  The
positions appearing in both families define a matching in `Gamma`, because
no head region or tail region can contain the same physical position as a
second region of its own type.  Therefore at most `nu(Gamma)` positions are
shared, and

\[
 N\ge2Q-\nu(\Gamma).                                 \tag{4.4}
\]

Substituting `Q=M-R` and `N=M+D` gives

\[
 D\ge M-2R-\nu(\Gamma).                              \tag{4.5}
\]

For the balanced bipartite graph with `Q` vertices on each side, Hall's
deficiency is

\[
 \Delta=\max_{S\subseteq E_R}(|S|-|N_\Gamma(S)|)
       =Q-\nu(\Gamma),                               \tag{4.6}
\]

so (4.5) is exactly `D>=Delta-R`.

This proof is correct.  Calling it an “exact labeled gate” should not be
misread as an if-and-only-if characterization of factorability or lower
target coverage.  It is the exact counting inequality for these `2Q`
chosen fresh demands; the graph may contain simultaneous-realizability
false positives and ignores other required labels.

## 5. Full verification of the A-turn

The selected middle row is

\[
 X_j=(a,j,2a-j)\quad(0\le j\le a),
 \qquad
 Y_s=(a-s,a,a+s)\quad(1\le s\le a),                 \tag{5.1}
\]

in that order.  It has `M=2a+1` distinct rank-`3a` targets.  Prescribe

\[
 I_i=[i,i+a],\qquad 1\le i\le M,                    \tag{5.2}
\]

on `N=M+a=3a+1` physical positions.

### 5.1 Factorability

For every coordinate threshold, inspect its incidence support in the
target row.

* The `x` coordinate is constant `a` along `X`, then decreases along `Y`.
  Every nonempty proper superlevel support is a prefix.
* The `y` coordinate increases from zero to `a` along `X`, then stays `a`
  along `Y`.  Every nonempty proper superlevel support is a suffix.
* The `z` coordinate decreases from `2a` to `a` along `X`, then increases
  from `a+1` to `2a` along `Y`.  A proper superlevel support is a union of a
  prefix and a suffix.

Thus no coordinate-threshold incidence word has a strictly internal run of
ones.  In particular it has no internal run shorter than the required
delay window `a+1`.  The fixed-window factorization criterion applies, and
the maximal factor

\[
 A_p=G_p:=\bigwedge_{i:p\in I_i}T_i                 \tag{5.3}
\]

satisfies

\[
 \bigvee_{p=i}^{i+a}A_p=T_i                         \tag{5.4}
\]

for every selected target.  All these entries are nonzero: every target in
the row has `z>=a`, hence every nonempty meet defining `G_p` has `z>=a`.
Every physical position belongs to at least one window.

This independently confirms that the example is an actual legal factor,
not merely an envelope-level compatibility drawing.

### 5.2 The shared entries

The transition `X_j -> X_{j+1}` starts at target index

\[
 i=j+1.
\]

Since the fixed windows shift by one, its new tail position is

\[
 p=i+a+1=a+j+2.                                      \tag{5.5}
\]

For `0<=j<=a-2`, the transition `Y_{j+1} -> Y_{j+2}` starts at exactly the
same target/physical index `p`, so `p` is its removed head position.

The selected windows containing `p` have target indices

\[
 p-a=j+2,\ldots,p=a+j+2,                             \tag{5.6}
\]

namely

\[
 X_{j+1},X_{j+2},\ldots,X_a,Y_1,\ldots,Y_{j+1}.
\]

Their coordinatewise meet is exactly

\[
 G_p=(a-j-1,j+1,a).                                  \tag{5.7}
\]

The `y=j+1` coordinate is the fresh increasing label of
`X_j -> X_{j+1}`, while `x=a-j-1` is the fresh decreasing label of
`Y_{j+1} -> Y_{j+2}`.  Since the actual maximal-factor entry is `A_p=G_p`,
both labels are genuinely achieved by the same position.  The `a-1`
positions obtained as `j=0,...,a-2` are distinct, so they form an explicit
matching of size `a-1` in `Gamma`.

The source note's A-turn certificate is therefore correct.

## 6. What the A-turn proves—and what it does not

It proves:

1. Counting one fresh head plus one fresh tail per internal ride transition
   and then summing those counts independently over rides is invalid.
2. At one turn, all but one of the first ride's `a` fresh tail positions can
   be reused by the `a-1` head demands internal to the second ride.
3. Pairwise cap compatibility is not merely a loose artifact here: the
   maximal factor realizes the sharing simultaneously.

It does not prove:

1. that the factor covers every below-middle target associated with either
   ride;
2. that the full local two-chain covering defect—not just its fresh
   middle-label subledger—can always be exported to the next ride;
3. that several A-turns can be concatenated cyclically while preserving all
   coordinate-run factorability conditions; or
4. that a complete `Theta(a)`-ride windmill has a near-perfect global
   compatibility matching.

Accordingly, the sentence “a three-direction windmill can continue the same
mechanism around successive A turns” must be marked conjectural until an
explicit cyclic row and factor are supplied.  The example is nevertheless
enough to defeat any proposed proof which charges the same fresh
head/tail loss separately at each ride.

## 7. Corrected theorem ledger

The durable conclusions are:

* **Proved:** the coarse label bounds (2.1), and the exact refinements
  (2.2)--(2.5).
* **Proved:** the `4a+1` portal realizes (3.3) target intervals through one
  labeled entry.  It is `Theta(ah)`-sharp, not constant-sharp for
  `h=Theta(a)`.
* **Proved:** fresh head and tail demands lie in disjoint same-type physical
  regions.
* **Proved:** the necessary matching/Hall bounds (4.4)--(4.6).
* **Proved:** the displayed delay-`a` A-turn is factorable and supplies an
  actual matching of size `a-1`.
* **Not proved:** simultaneous embeddability of many portal arms, additive
  or nonadditive behavior of the complete below-middle two-chain defect,
  continuation around a full windmill, or a quadratic Hall deficiency for
  every global ride system.

The two proposed next routes remain legitimate, with slightly narrower
interpretations:

1. Prove a quadratic Hall deficiency for the **fresh-demand graph** of every
   candidate global windmill.  This would force quadratic `D` by (4.5), but
   the A-turn shows the deficiency cannot be summed locally.
2. Prove a global portal-arm contamination theorem.  The standalone portal
   shows why a per-entry capacity bound cannot work, but gives no global
   arm-sharing construction.

Neither route is settled by the examples in the source note.
