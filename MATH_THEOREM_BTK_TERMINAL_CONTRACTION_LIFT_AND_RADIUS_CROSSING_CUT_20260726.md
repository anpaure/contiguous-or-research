# BTK terminal contractions: exact annular lifts and the peak-radius crossing cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, web input,
or entropy argument is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=\lceil m^{1/4}\rceil,
 \qquad H=\left\lfloor\sqrt{m\log m}\right\rfloor.
\tag{0.1}
\]

Retain the chains of the standard BTK SCD having native radius at least
\(q_0\). Their number is

\[
 N_{q_0}=\binom{2m}{m-q_0}=(1-o(1))W,
\tag{0.2}
\]

whereas

\[
 N_H=\binom{2m}{m-H}=(1+o(1)){W\over m}.
\tag{0.3}
\]

Thus the requested path scale

\[
 O\left({W\over m}\operatorname{polylog}m\right)
 =o(W/H)
\tag{0.4}
\]

is numerically consistent with a bounded-polylogarithmic number of paths
per full-top fibre.

This note proves two exact facts and one obstruction.

1. The known suffix rule
   \[
   S**\longrightarrow S01
   \tag{0.5}
   \]
   is not confined to native radii at least \(H\). At native target
   radius \(d\ge H\) it is a genuine clipped radius-\(H\) rotor. At every
   \(q_0\le d<H\) it has explicit annular-compatible radius-\(H\)
   extensions joined by one promotion. Successive right-terminal
   contractions have one coherent sequence of collars, preserving all
   inner BTK flags.

2. Reverse-complement duality gives the directed prefix rule
   \[
   01S\longrightarrow **S,
   \tag{0.6}
   \]
   only in the rotor range \(d\ge H\). It does **not** give a short-chain
   promotion lift. For \(q_0\le d<H\), the canonical prefix pair has no
   annular-compatible bridge-one edge in this direction.

3. A hierarchy using only (0.5), or any other strictly native-radius-
   decreasing contractions, cannot approach (0.4). If \(p\) is its path
   count, then
   \[
   \boxed{
   p\ge
   \left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
   \tag{0.7}
   \]

More generally, let \(b_d\) count selected radius-increasing crossings
adjacent to native radius \(d\). Every directed path forest satisfies

\[
 \boxed{p+b_d\ge c_d,}
\tag{0.8}
\]

where \(c_d\) is the number of native radius-\(d\) chains. At the peak
\(d_*=\sqrt{m/2}+O(1)\), a successful hierarchy needs

\[
 \boxed{
 b_{d_*}\ge
 \left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
\tag{0.9}
\]

Since \(d_*<H\), the base suffix/prefix catalogue has no increasing edge
at either boundary adjacent to \(d_*\). Thus it obeys the full lower bound
(0.7), even if both formal terminal orientations are included.

Thus a successful terminal-block hierarchy must create an essentially
full upward crossing matching at the Gaussian peak by using deeper nested
blocks. Counting the \(1/4\) top-tail matching repeatedly without proving
this state-composable crossing property cannot yield (0.4).

No full hierarchy is constructed here. The positive advance is the exact
short-chain collar recursion; the negative result closes the one-sided
and single-outer-pair recursions.

## 1. BTK terminal normal form

Use the BTK convention in which every fixed \(01\) pair is matched. A
chain of radius \(d+1\) has free positions

\[
 u_1<\cdots<u_{2d}<a<b,
\tag{1.1}
\]

where \(a,b\) are the last two free positions. Fixed words between
consecutive free positions and after \(b\) are balanced. Turning \(a,b\)
into an outer matched \(0,1\) pair therefore gives another valid BTK
signature. Denote the chains by

\[
 C_*:\ S*D*Q,
 \qquad
 C_{01}:\ S0D1Q,
\tag{1.2}
\]

where \(D,Q\) are fixed balanced BTK words. The literal rule
\(S**\to S01\) is \(D=Q=\varnothing\).

Let \(I,O\) be the common fixed-in and fixed-out sets before the change.
Then

\[
 \rho(C_*)=d+1,\qquad \rho(C_{01})=d,
\tag{1.3}
\]

and the target has fixed-in set \(I+\{b\}\), fixed-out set \(O+\{a\}\),
and free word \(u_1,\ldots,u_{2d}\).

This last-two-free contraction is canonical and may be repeated. Fixed
balanced words accumulated on the right merely join \(I,O\).

## 2. Exact lift above and below the collar radius

### Theorem 2.1 (terminal contraction bridge)

For every \(d\ge q_0\), the directed contraction

\[
 C_*\longrightarrow C_{01}
\tag{2.1}
\]

has annular-compatible radius-\(H\) states joined by one bridge-one arc.

* If \(d\ge H\), the forced clippings are joined by a genuine rotor.
* If \(q_0\le d<H\), explicit radius-\(H\) extensions are joined by a
  promotion and retain every actual BTK flag through depth \(d\).

#### Proof in the rotor range

Assume \(d\ge H\). The source clipped lower part is

\[
 L_*=I+\{u_1,\ldots,u_{d+1-H}\}.
\tag{2.2}
\]

Choose

\[
 x=u_{d+1-H},\qquad y=b.
\tag{2.3}
\]

The full rotor produces

\[
 L_*-x+b
 =I+b+\{u_1,\ldots,u_{d-H}\},
\tag{2.4}
\]

the collar

\[
 u_{d-H+1},\ldots,u_{d+H},
\tag{2.5}
\]

and the residual

\[
 O+a+\{u_{d+H+1},\ldots,u_{2d}\}.
\tag{2.6}
\]

These are exactly the forced clipping data of \(C_{01}\).

#### Proof in the promotion range

Assume \(q_0\le d<H\), and put

\[
 h=H-d-1.
\tag{2.7}
\]

Choose ordered distinct lists

\[
 \alpha=(\alpha_1,\ldots,\alpha_h)\subset I,
 \qquad
 \beta=(\beta_1,\ldots,\beta_h)\subset O.
\tag{2.8}
\]

The source extension is

\[
 \omega_*=
 (I\setminus\alpha;\
   \alpha,u_1,\ldots,u_{2d},a,b,\beta;\
   O\setminus\beta).
\tag{2.9}
\]

Choose \(x\in I\setminus\alpha\). In (2.9), coordinate \(b\) has position

\[
 j=h+2d+2=H+d+1>H.
\tag{2.10}
\]

Promote \(b\) with departure \(x\). The successor is

\[
 \omega_{01}=
 (I\setminus\alpha-x+b;\
   x,\alpha,u_1,\ldots,u_{2d},a,\beta;\
   O\setminus\beta).
\tag{2.11}
\]

This is precisely the extension of \(C_{01}\) whose lower extension order
is \((x,\alpha)\) and whose upper extension order is \((a,\beta)\).
Its central word remains \(u_1,\ldots,u_{2d}\). Thus every native BTK
flag is unchanged, and (2.11) is the literal promotion formula.
\(\square\)

### Corollary 2.2 (coherent repeated right contraction)

Start with one BTK signature of radius \(r\ge q_0\), and repeatedly
contract its last two free positions until radius \(q_0\). The resulting
chain sequence admits one coherent annular-compatible bridge path.

#### Proof

Above \(H\), forced clippings compose. At the first step below \(H\),
formula (2.11) has lower extension prefix \((x,\alpha)\) and upper
extension suffix \((a,\beta)\). These are exactly the lists used when the
target becomes the next source. Each later contraction prepends one new
lower departure and moves its newly fixed-out coordinate to the front of
the upper extension list. Induction gives one common state at every
join. \(\square\)

Thus pairwise collar existence is not the issue for the one-sided
terminal recursion: its states really compose.

## 3. The directed dual and the short-chain asymmetry

Write \(\bar i=2m+1-i\), and apply the bar entrywise to sets and words.
Let \(J\) be the reverse-complement chain involution: it interchanges the
lower and residual blocks and reverses the reflected singleton word,

\[
 J(L;z_1,\ldots,z_{2H};R)
 =(\bar R;\bar z_{2H},\ldots,\bar z_1;\bar L).
\tag{3.1}
\]

Reverse-complement preserves the standard BTK signature family.

### Lemma 3.1 (rotor anti-automorphism)

If \(\omega\to\omega'\) is a rotor, then

\[
 J(\omega')\longrightarrow J(\omega)
\tag{3.2}
\]

is a rotor.

#### Proof

Substitute

\[
 \omega'=(L-x+y;\
 x,z_1,\ldots,z_{2H-1};\
 R-y+z_{2H})
\]

into (3.1). Starting from \(J(\omega')\), choose departure
\(\bar z_{2H}\) and entry \(\bar x\); the rotor formula gives
\(J(\omega)\).
\(\square\)

Applying \(J\) to the rotor-range part of Theorem 2.1 yields

\[
 \boxed{01S\longrightarrow **S,}
\tag{3.3}
\]

when the smaller native radius \(d\) is at least \(H\). This edge
increases native radius by one. It is not the reverse of (2.1) on the
same signatures.

Promotion is different: \(J\) reverses a promotion state pair, but the
reversed pair is neither a rotor nor a promotion in general. The failure
is forced by the short-chain BTK flags.

### Theorem 3.2 (no canonical prefix expansion below \(H\))

Let \(q_0\le d<H\). Consider the two BTK chains

\[
 C_{01}:01S,\qquad C_*:**S,
\tag{3.4}
\]

of native radii \(d\) and \(d+1\), respectively. There is no
annular-compatible radius-\(H\) bridge-one arc

\[
 C_{01}\longrightarrow C_*.
\tag{3.5}
\]

This remains true after arbitrary legal choices of their outer extension
orders and their invisible inner \(q_0\)-port orders.

#### Proof

Write the first two free coordinates of \(C_*\) as \(a<b\), and its
remaining free word as \(u_1,\ldots,u_{2d}\). Before changing the pair,
let \(I,O\) be the common fixed-in and fixed-out sets. Then \(C_{01}\)
has fixed-in set \(I+b\), fixed-out set \(O+a\), whereas \(C_*\) has
bottom set \(I\) and has \(a\) as a forced free coordinate.

The canonical BTK middle owners illustrate the forced exchange:

\[
 X=I+b+\{u_1,\ldots,u_d\},
\tag{3.6}
\]

\[
 Y=I+\{a,b,u_1,\ldots,u_{d-1}\}.
\tag{3.7}
\]

Thus \(Y=X-u_d+a\).

More generally, the conclusion that \(a\) enters is independent of the
middle-corner choice. For \(C_{01}\), coordinate \(a\) is fixed out and
does not belong to its depth-\(q_0\) upper endpoint. Hence no legal source
corner contains \(a\). For \(C_*\), coordinate \(a\) is the first free
coordinate and \(d+1>q_0\), so it already belongs to the depth-\(q_0\)
lower endpoint. Hence every legal target corner contains \(a\). If the
two corners are not Johnson adjacent there is no bridge. If they are,
their unique entering coordinate is necessarily \(a\).

In every distinct-owner bridge-one transition, the entering owner
coordinate is inserted into the target lower collar block: it is the
residual entry of a rotor or the promoted singleton of a promotion. Hence
(3.5) would force \(a\) into that lower block.

But every annular-compatible radius-\(H\) state of \(C_*\) has lower
block contained in its native bottom \(I\). The coordinate \(a\) is a
forced outer BTK chain singleton (its depth is \(d+1>q_0\)), so neither an
outer extension choice nor an inner \(q_0\)-reordering may move it into
that lower block. This is a contradiction.

This contradicts annular compatibility, completing the proof.
\(\square\)

The asymmetry is exact: right-terminal contraction survives below \(H\)
as a promotion, while its formal left-terminal dual does not survive as
a forward bridge.

## 4. Exact native-radius census

Let \(c_d=c_d^{(m)}\) be the number of native radius-\(d\) BTK chains.
Every SCD has the same census:

\[
 \boxed{
 c_d=N_d-N_{d+1}
 =N_d{2d+1\over m+d+1}.}
\tag{4.1}
\]

The consecutive ratio is

\[
 {c_{d+1}\over c_d}
 ={(m-d)(2d+3)\over(2d+1)(m+d+2)}.
\tag{4.2}
\]

Hence the maximum occurs at

\[
 d_*=\sqrt{m/2}+O(1).
\tag{4.3}
\]

Since \(q_0=o(\sqrt m)\) and \(H/\sqrt m\to\infty\), this peak is
retained. Moreover,

\[
 \boxed{
 c_{d_*}
 =\left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
\tag{4.4}
\]

## 5. The one-sided hierarchy obstruction

### Theorem 5.1 (complete decreasing-relaxation cut)

Every directed path cover of the retained chains using only arcs which
strictly decrease native radius has

\[
 \boxed{p\ge c_{d_*}.}
\tag{5.1}
\]

This remains true after adding every possible edge from every larger
radius to every smaller radius and discarding all collar constraints.

#### Proof

A strictly decreasing path contains at most one radius-\(d_*\) vertex.
\(\square\)

Equations (4.4)--(5.1) prove (0.7). In particular, Corollary 2.2 cannot
be assembled into the requested number of components without
radius-increasing bridges.

### Theorem 5.2 (peak crossing inequality)

Let \(F\) be a directed path forest. Fix \(d\), and let \(b_d(F)\) be the
number of selected upward arcs of types \(d-1\to d\) and \(d\to d+1\)
when all radius changes are adjacent. More generally count the first
upward crossing of one of these two boundaries between consecutive visits
of a path to radius \(d\). Then

\[
 \boxed{p+b_d(F)\ge c_d.}
\tag{5.2}
\]

#### Proof

Charge the first radius-\(d\) visit on a path to that path. Between every
two later consecutive visits, the path either went below \(d\) and
crossed upward into \(d\), or went above \(d\) through an upward crossing
out of \(d\). Charge the later visit to the first such crossing. Distinct
visits use disjoint path intervals and hence distinct selected arcs.
\(\square\)

At \(d=d_*\), (4.4)--(5.2) give (0.9) whenever
\(p=o(W/H)\).

## 6. The base terminal hierarchy still fails

At the peak radius \(d_*=\sqrt{m/2}+O(1)\), both adjacent native radii are
strictly below \(H\). Theorem 3.2 therefore removes every increasing
prefix edge (3.3) across those two boundaries. The suffix rule and all its
coherent repetitions decrease native radius. Hence Theorem 5.2 has
\(b_{d_*}=0\), and the complete base terminal hierarchy satisfies

\[
 \boxed{
 p\ge c_{d_*}
 =\left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
\tag{6.1}
\]

This is stronger than the purely signature-counting \(1/4+1/4\) estimate:
the apparent second quarter is not a legal forward bridge after the
short-chain flags are installed.

A successful recursive terminal-block catalogue must therefore introduce
genuinely different increasing rules whose selected upward crossings
cover all but

\[
 O\left({W\over m}\operatorname{polylog}m\right)
\tag{6.2}
\]

of the peak-radius chains.

## 7. Exact remaining recursive gate

Let \(\mathscr U_d\) be the catalogue of proposed state-composable
radius-increasing terminal-block bridges adjacent to radius \(d\). The
first unavoidable peak condition is

\[
 \boxed{
 \nu(\mathscr U_{d_*-1}\cup\mathscr U_{d_*})
 \ge c_{d_*}
 -O\left({W\over m}\operatorname{polylog}m\right),}
\tag{7.1}
\]

where the matching is on split copies of actual selected BTK states. A
count of signature blocks is insufficient: the same radius-\(H\)
extension must support both the incoming and outgoing edge at an internal
path vertex.

Even (7.1) is not sufficient. The union of upward and downward matchings
must be acyclic after one common ordering and cover every native radius
simultaneously. Equivalently, the full catalogue needs

\[
 \boxed{
 \max_A\bigl(|A|-|N_\prec(A)|\bigr)
 =O\left({W\over m}\operatorname{polylog}m\right).}
\tag{7.2}
\]

Theorem 2.1 supplies the coherent downward half of this graph. Lemma 3.1
supplies upward atoms only above \(H\), outside the peak cut. The missing
theorem is a new nested increasing block move below \(H\), followed by a
selection attaining (7.1)--(7.2) without assigning two incompatible
collars to one chain.

## 8. Proved boundary

Proved here:

1. every last-two-free BTK contraction has an exact bridge through the
   full range \(d\ge q_0\);
2. below \(H\) it is an explicit promotion preserving all inner flags;
3. repeated right contractions admit one coherent collar history;
4. reverse-complement gives directed prefix rotors only above \(H\), and
   the corresponding short-chain prefix expansion is impossible;
5. every one-sided contraction hierarchy has
   \(\Omega(W/\sqrt m)\) paths; and
6. the complete base suffix/prefix hierarchy still leaves
   \((\sqrt{2/e}+o(1))W/\sqrt m\) paths.

Not proved here:

1. nested prefix atoms with the near-saturating peak crossing matching
   (7.1);
2. a common collar choice at every alternating up/down internal vertex;
3. the global ordered-Hall estimate (7.2); or
4. coefficient one.

The explicit BTK lane is not closed, but the proposed base hierarchy is.
The suffix rule solves coherent descent and supplies the known \(1/4\)
top-tail sector. Coefficient one would require a new flag-compatible
radius-increasing terminal move below \(H\), crossing the peak radius
almost bijectively; reverse-complement of the suffix promotion is not
such a move.
