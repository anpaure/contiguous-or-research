# Three `C10` switches repair the standard `m=5` Catalan state

Date: 2026-07-31  
Status: exact finite positive theorem; complete one-hex and bounded-switch
calibration at the displayed standard output; no uniform all-`m` packet
theorem

## 0. Verdict

The unmodified standard `m=5` plane-tree gluing family is not decorable, but
its failure is repairable by a packet of bounded-port switches which preserves exactly the
private state sought by the recursion.

Start from the locally transparent standard Hamilton output using labels

\[
 (11001010,10101010),\qquad(11001100,10101100).
\]

It misses the lower colours `73,146,292`, their three complementary upper
colours, and has augmented trace deficiency three.  There are three
vertex-disjoint Hamilton-safe `C10` switches under which

\[
             (3,3,3)\longrightarrow(2,2,2)
             \longrightarrow(1,1,1)\longrightarrow(0,0,0),       \tag{0.1}
\]

where the coordinates are lower-palette deficit, upper-palette deficit, and
joint alternating-SDR deficiency.

The final Hamilton cycle has a joint alternating SDR which can be forced to
mark all twelve ports of the two original standard hexagons.  The same marks
are leaf-peelable on all four states obtained by independently toggling the
two standard hexagons.  Their private lower-owner paths are exactly

\[
 [82]-g-[84]-g-[88],\qquad [50]-g-[52]-g-[56].       \tag{0.2}
\]

Thus item 2172 refutes the *unmodified* standard induction, while this
theorem gives its first exact corrected form:

> preliminary bounded turn-palette repair, followed by transparent private
> plane-tree gluing.

The missing all-`m` theorem is now a uniform existence theorem for such
repair packets; the private-triple mechanism itself survives the first
failure.

## 1. Exact short-switch negatives

For the locally transparent standard output, among all `1,680` incidence
hexagons, `129` alternate with the Hamilton cycle and `22` are Hamilton-safe.
Their exact `(lower missing, upper missing, joint deficiency)` histogram is

\[
 (3,3,3)^9(3,3,4)^{11}(3,4,4)^1(4,4,4)^1.          \tag{1.1}
\]

So no one-hex switch improves either palette.  The other standard Hamilton
output has `25` safe incidence hexagons; `22` retain deficits `(3,3)`, and
the other three worsen one or both palettes.

The exact Hamilton-safe incidence-hex BFS from the transparent output is

\[
\begin{array}{c|r|c|r}
 \text{depth}&\text{new cycles}&\text{best palette deficits}&
 \#\text{ at best}\\ \hline
 1&22&(3,3)&20\\
 2&1139&(2,2)&3\\
 3&44478&(2,2)&231.
\end{array}                                           \tag{1.2}
\]

Hence no sequence of at most three incidence-hex toggles repairs the turn
palettes.

The longer one-switch census is also exact:

* `181` alternating `C8` circuits, `41` Hamilton-safe; best deficit
  `(2,3,3)`;
* `1,592` alternating `C10` circuits, `654` Hamilton-safe; best deficit
  `(2,2,2)`, attained by `31` circuits.

No single `C6`, `C8`, or `C10` is enough.  The repair is genuinely compound.

## 2. The explicit three-switch staircase

The three `C10` edge sets are

```text
C1:
(15,79) (15,271) (267,271) (267,331) (77,79)
(77,109) (105,109) (105,361) (329,331) (329,361)

C2:
(147,155) (147,211) (209,211) (209,241) (154,155)
(154,218) (216,218) (216,248) (240,241) (240,248)

C3:
(141,173) (141,397) (389,397) (389,421) (172,173)
(172,188) (180,188) (180,436) (420,421) (420,436)
```

They have pairwise disjoint vertex sets.  At every stage the next circuit
alternates with the current Hamilton cycle and its toggle remains Hamilton.
The missing colours evolve as

\[
\begin{array}{c|c|c}
 &\text{missing lower}&\text{missing upper}\\ \hline
 C_0&73,146,292&219,365,438\\
 C_1&146,292&219,438\\
 C_2&292&438\\
 C_3&\varnothing&\varnothing.
\end{array}                                           \tag{2.1}
\]

Since

\[
 511-73=438,\qquad511-146=365,\qquad511-292=219,
\]

the packet routes the period-three lower orbit into the complementary upper
orbit with a cyclic offset: the first switch repairs lower `73` and upper
`365`, the second repairs `146` and `219`, and the third repairs `292` and
`438`.  This orbit-staircase organization is the structural content of the
certificate, not just its existence.

## 3. Joint alternating SDR and common-core linkage

The final augmented trace graph has a perfect matching of order `210` even
after forcing all twelve standard hexagon ports to be selected.  The induced
sets contain `84` marked vertices on each shore and form a valid alternating
decoration.

Intersect the original and repaired augmented trace graphs.  This common
core has matching order `197`, hence deficiency `13`.  Relative to an exact
maximum common-core matching and the forced-port final perfect matching,
the symmetric difference contains exactly thirteen vertex-disjoint
augmenting paths (and harmless alternating cycles).  This is the literal
common-core linkage certificate required by the bounded-switch theorem: no
new Hall-cut assertion is being inferred from palette counts alone.

The final gap-colour graph is a forest and its perfect matching is unique.
Its binary mark trace is also on the linear-forest side.

## 4. The private triples survive

Apply the three `C10` switches to the base factor before the two standard
hexagons.  The repaired preglue factor has components of orders `120` and
`132`.  With the one forced-port decoration fixed, all four points of the
two-standard-hexagon cube are valid leaf-peelable decorated states:

\[
 (0,0),\ (1,0),\ (0,1),\ (1,1).
\]

For the first standard label, the three old singleton sockets are

\[
                       \{82\},\{84\},\{88\}.
\]

After toggling, the relevant sockets are

\[
                       \{82,84\},\{84,88\},\{88\},
\]

which is precisely the attachment path

\[
                       [82]-g-[84]-g-[88].
\]

For the second label the corresponding transition is

\[
 \{50\},\{52\},\{56\}
 \longrightarrow
 \{50,52\},\{52,56\},\{56\},
\]

giving `[50]-g-[52]-g-[56]`.  The two owner triples are disjoint.  Thus the
repair packet does not merely restore turn surjectivity: it restores a
joint decoration on the exact private-socket face proposed for recursive
composition.

## 5. Scope and corrected target

This is an exact theorem at `m=5`.  It proves neither that three `C10`s
always suffice nor that the missing orbit is always divisor-periodic.  What
it does prove is strategically sharp:

1. standard plane-tree gluing without repair fails at the first new case;
2. no single local `C6/C8/C10` switch completes the repair there;
3. a controlled-debt packet of bounded-port switches repairs the entire joint state; and
4. the private-triple attachment survives that repair exactly.

The corrected inductive target is therefore a **palette-repair packet plus
private gluing theorem**, not the unmodified standard private-triple
conjecture.

## 6. The divisor/necklace law and a precise next conjecture

The occurrence of the three-colour defect at `m=5` is not numerology.  Put

\[
                         k=2m-1.
\]

The lower and upper turn-colour ranks are `m-2` and `m+1`.  Therefore

\[
 \gcd(k,m-2)=\gcd(3,m-2),\qquad
 \gcd(k,m+1)=\gcd(3,m+1).                            \tag{6.1}
\]

The two gcds agree.  Apart from the trivial extreme palettes at `m=2`, the
rotation action on both turn-colour levels is free unless

\[
                         m\equiv2\pmod3.             \tag{6.2}
\]

At `m=3` and `m=4`, the relevant ranks are coprime to ground-set sizes `5`
and `7`; the positive standard fixtures need no divisor packet.  At `m=5`,
ground size `9` is the first case with a proper nonfree turn-colour orbit,
and the first standard-family failure is exactly

\[
 {cal O}=\{73,146,292\}
          =\{100100100,010010010,001001001\}.         \tag{6.3}
\]

The repair pairs are cyclically offset:

\[
\begin{array}{c|c|c|c}
 &\text{lower repaired}&\text{upper repaired}&
   \text{common rank-}(m-3)\text{ core}\\ \hline
 C_1&73&\overline{146}=365&\{0,3\},\\
 C_2&146&\overline{292}=219&\{4,7\},\\
 C_3&292&\overline{73}=438&\{2,7\}.
\end{array}                                           \tag{6.4}
\]

The first two cores lie inside the lower colour they repair.  The third is a
relay core: it takes one coordinate from the last lower target and one from
the preceding orbit class.  This agrees with topology: `C3` alone splits the
Hamilton cycle, whereas after `C1,C2` it is the final reconnecting switch.
Thus the packet is not three independent orbit copies; it is a linked
orbit router.

There is an exact comparison with
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md`.  At `q=9,a=1`,
that theorem gives

\[
 2\operatorname {Cat}_1=2
 \quad\text{exceptional partial-orbit filters},
 \qquad
 2\operatorname {Cat}_1+1=3
 \quad\text{globally}.                               \tag{6.5}
\]

The switch cube realizes the same `2+1` division in topology.  `C1` and
`C2` are individually Hamilton-safe and have pure cores contained in the
periodic lower classes they repair.  `C3` is not Hamilton-safe alone: the
component counts for subsets `000,001,...,111` are

\[
                        1,1,1,1,2,3,2,1.             \tag{6.6}
\]

Its mixed core is the relay which becomes Hamilton-safe only after both
direct filters are installed.  In that exact sense, `C1,C2` play the two
exceptional-filter roles and `C3` plays the congruence-forced ordinary
bridge role.

This is a role classification, not a literal bijection between switches and
the partial edge-orbits in the period-three theorem.  The thirty toggled
incidence edges occupy eighteen full-rotation edge orbits.  Moreover every
one of the three switches repairs one physical colour on each exceptional
shore.  The period-three theorem concerns the selected final edge set,
whereas a `C10` is a symmetric-difference operation.  Equation (6.5)
therefore explains the observed `2+1` role split and the third switch's
topology;
it does not identify one `C10` with one partial orbit.

The distinction can be measured on the actual forced-port decoration.
Reconstructing its complete `210`-edge perfect diamond matching gives `67`
used full-rotation orbits, only `2` full and `65` partial.  The partial
orbits split as

\[
 2\text{ lower-exceptional},\qquad
 2\text{ upper-exceptional},\qquad
 61\text{ nonexceptional}.                            \tag{6.7}
\]

So this particular decoration is very far from attaining Corollary 2.1's
three-partial-orbit lower bound.  The numerical equality “three switches,
global floor three” reflects the minimal *repair-role* decomposition found
here, not symmetry-optimal orbit support.  Attaining the period-three orbit
floor would require a much more equivariant representative choice than the
forced matching used in this certificate.

The exact finite theorem suggests the following deliberately scoped target.

> **Stabilizer-three necklace repair-packet conjecture.**  Let
> `m=2 (mod 3)`, `k=2m-1=3q`, and suppose a recursively supplied
> middle-levels factor has all free turn-colour orbits covered while its
> residual empty occurrence classes are one stabilizer-three lower necklace
> orbit
> \({\cal O}=(L_j)_{j\in\mathbb Z_q}\) and its complementary upper orbit.
> Suppose also that the private gluing collars are disjoint from a repair
> bank.  Then there is an ordered packet of `q` bounded alternating
> pentagons such that step `j` introduces `L_j` and
> \(\overline{L_{j+1}}\) without losing any previously covered turn colour,
> the packet has a Hamilton-safe ordering and an exact common-core
> augmenting linkage, its rank-`m-3` cores form a relay chain inside adjacent
> orbit classes, and the final perfect matching can retain the private collar
> marks.

For `m=5`, `q=3`, Sections 2--4 prove every clause.  For `m=3,4` the
hypothesis is empty because all proper turn-colour necklaces are free; for
`m=2` the two palettes are the trivial fixed empty/full colours.  No test at
the next nonfree case `m=8` has been made, so the boxed statement is a
candidate induction lemma, not a theorem.

The packet is atomic: its intermediate Hamilton cycles are not accepting
decorated states.  Only the final endpoint, together with its explicit
common-core augmenting linkage and retained private ports, is a valid
regeneration boundary.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_standard_m5_three_c10_private_repair_20260731.py
```

The audit reconstructs both standard Hamilton outputs, the complete
one-incidence-hex censuses, the depth-three incidence-hex BFS, all alternating
`C8/C10` switches at the transparent root, the displayed three-switch
certificate, a forced-port perfect matching, the common-core linkage, all
four standard-glue states, and both private attachment paths.  Its frozen
output is

```text
scratch/catalan_standard_m5_three_c10_private_repair_20260731.audit.json
```
