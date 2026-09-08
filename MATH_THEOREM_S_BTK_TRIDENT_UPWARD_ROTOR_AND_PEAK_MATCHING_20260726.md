# The BTK trident upward move: exact low-radius rotors, promotions, and peak matching capacity

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \gamma_q=N_q-N_{q+1},
\]

and fix \(1\le H<m\).  Let a BTK target chain have native radius
\(d+1\), where \(0\le d<H\), and begin in signature form as

\[
                         P\,*_t\,R\,*_\beta\,S\,U.
\tag{0.1}
\]

Here \(P,R,S\) are Dyck words and \(U\) denotes the rest of the
signature, beginning with the remaining \(2d\) free stars.  Choose a
closing coordinate \(y\), that is, a letter \(1\), in a nonempty \(P\).
Change the three displayed statuses by

\[
             y:1\longmapsto0,qquad *_t\longmapsto1,qquad
             *_\beta\longmapsto1.
\tag{0.2}
\]

The resulting source prefix is

\[
                  P^{(y:1\to0)},1_t,R,1_\beta,S,
\tag{0.3}
\]

and is a valid Dyck word.  Thus (0.3) defines a BTK source chain of native
radius \(d\).

The exact conclusions are:

1. The source and target admit a directed radius-\(H\) rotor from radius
   \(d\) upward to radius \(d+1\).  The rotor frees \(t,\beta\), moves
   \(y\) from source fixed-out to target fixed-in, and is flag-coherent at
   both native chains.

2. At the boundary \(d=H-1\), the departure is \(t\); only \(\beta\)
   lies in the source's one-coordinate artificial lower list.  Thus the
   informal assertion that the lower artificial list always ends in
   \((t,\beta)\) requires this correction.

3. The same signature pair has directed promotions: put \(y\) in the
   source upper artificial list and omit it.  These are precisely the
   upper-deleting promotions in the upward class.  A promotion which
   deletes an old source free coordinate is BTK-invalid.

4. Conversely, every coherent low-radius upward rotor has exactly the
   trident form (0.1)--(0.3).  The same is true of every upward promotion
   after the impossible lower-list and old-free deletion cases are
   removed.

5. The exact number of eligible target chains at boundary
   \(d\to d+1\) is
   \[
       \boxed{E_d={d+2\over m}N_{d+2}.}
   \tag{0.4}
   \]
   Counting a target once for each eligible choice of \(y\), the number
   of marked chain pairs is exactly
   \[
                              \boxed{N_{d+2}.}
   \tag{0.5}
   \]

6. There is an explicit owner-injective subfamily.  Require
   \[
                         P=(01)^k,\qquad k\ge1,
   \tag{0.6}
   \]
   and take \(y\) to be the last \(1\) of \(P\).  Its size is
   \[
    \boxed{
     M_d=[z^{m-d-1}]{z\over1-z}C(z)^{2d+2}.}
   \tag{0.7}
   \]
   where \(C(z)=1+zC(z)^2\).  If \(d\sim\sqrt{m/2}\), then
   \[
                         M_d=\left({1\over6}+o(1)\right)\gamma_{d+1}.
   \tag{0.8}
   \]

7. At a peak radius, the incoming and outgoing copies of (0.6) are
   disjoint and together occupy \((1/3+o(1))\gamma_d\) chains.  The bank
   is therefore a matching bank, not a long alternating path factor.

8. Below the clipping boundary there are no larger upward jumps: every
   coherent bridge from radius \(d\) to radius \(e>d\), with
   \(e\le H\), has \(e=d+1\) and is a trident.  If \(h_d\) is the
   number of selected same-radius arcs at the peak, every directed path
   forest on the full BTK census obeys the exact bound
   \[
      p+h_d\ge q_d+e_d-\gamma_d-N_{H+1}.
   \]
   At the calibrated \(H\), this is
   \((1/6+o(1))\gamma_d\).  Thus the trident family supplies genuine
   \(\Theta(W/\sqrt m)\) upward density, but a standard-BTK solution still requires
   \(\Theta(W/\sqrt m)\) horizontal bridges of a different kind.

The construction is a genuine new low-radius upward bridge family.  It
does not by itself prove a path cover with \(o(W/H)\) components.

## 1. Signature legality

Use height \(+1\) for a zero and \(-1\) for a one.  A Dyck word has
nonnegative partial heights and final height zero.  In \(P\), change the
chosen down-step \(y\) to an up-step.  Every height from \(y\) to the end
of \(P\) increases by two, so the modified word remains nonnegative and
ends at height two.  The new letter \(1_t\) lowers the height to one;
the Dyck word \(R\) stays at or above one; and \(1_\beta\) returns to
zero.  Finally \(S\) is Dyck at baseline zero.  Hence (0.3) is Dyck.

Let \(I,O\) be the target's fixed-in and fixed-out sets.  Thus
\(y\in I\), while \(t,\beta\) are target-free.  The source fixed sets are
exactly

\[
 I_s=I-\{y\}+\{t,\beta\},\qquad
 O_s=O+\{y\}.
\tag{1.1}
\]

Both have size \(m-d\), as required for a radius-\(d\) chain.  The source
free word is the old target tail

\[
                         U=(u_1,\ldots,u_{2d}).
\tag{1.2}
\]

## 2. Exact rotor collars

Put

\[
                         s=H-d.
\tag{2.1}
\]

The target fixed sets \(I,O\) have size \(m-d-1\).

### Theorem 2.1 (trident rotor, interior artificial case)

Assume \(s\ge2\).  Choose an ordered target lower artificial tuple

\[
 A=(x,C_0),\qquad |C_0|=s-2,
\tag{2.2}
\]

from \(I-\{y\}\), and choose an ordered \(s\)-tuple

\[
                         D=(B,z)
\tag{2.3}
\]

from \(O\), where \(|B|=s-1\).  Define

\[
 \omega_s=
 (I-\{y\}-C_0;\ C_0,t,\beta,U,B,z;\
  O+\{y\}-B-\{z\})
\tag{2.4}
\]

and

\[
 \omega_t=
 (I-A;\ A,t,\beta,U,B;\ O-B).
\tag{2.5}
\]

Then the full rotor from \(\omega_s\), with departure \(x\) and entry
\(y\), is exactly \(\omega_t\).

#### Proof

The source lower artificial tuple is \((C_0,t,\beta)\), of length \(s\),
and its upper tuple is \((B,z)\), also of length \(s\).  Thus (2.4) is a
coherent extension of the radius-\(d\) source.  Equation (2.5) has
artificial tuples \(A,B\), both of length \(s-1\), and is a coherent
extension of the radius-\(d+1\) target.

Apply

\[
 (L;z_1,\ldots,z_{2H};R)
 \longmapsto
 (L-x+y;\ x,z_1,\ldots,z_{2H-1};\ R-y+z_{2H}).
\tag{2.6}
\]

The lower block becomes

\[
 I-\{y\}-C_0-\{x\}+\{y\}=I-A.
\]

The collar becomes

\[
 (x,C_0,t,\beta,U,B)=(A,t,\beta,U,B),
\]

and the residual block becomes

\[
 O+\{y\}-B-\{z\}-\{y\}+\{z\}=O-B.
\]

These are all three parts of (2.5). \(\square\)

### Theorem 2.2 (the boundary \(d=H-1\))

When \(s=1\), choose \(z\in O\).  Then

\[
 (I-\{y\}+\{t\};\ \beta,U,z;\ O+\{y\}-\{z\})
 \longrightarrow
 (I;\ t,\beta,U;\ O)
\tag{2.7}
\]

is the full rotor with departure \(t\) and entry \(y\).

#### Proof

The source has one artificial lower coordinate, namely \(\beta\), and
one artificial upper coordinate \(z\).  Its lower block contains \(t\).
Substitution in (2.6) gives (2.7) verbatim. \(\square\)

The two cases give the unified rotor-collar count for one marked signature
pair:

\[
 \boxed{
 R^{\rm ext}_{d,H}
 =(m-d-2)_{s-1}(m-d-1)_s.}
\tag{2.8}
\]

The convention \((a)_0=1\) makes (2.8) valid at \(s=1\), where it equals
\(m-H\).

## 3. Exact promotions and necessity

For \(s\ge2\), retain \(A=(x,C_0)\) as in (2.2), choose an ordered
\((s-1)\)-tuple \(B\) from \(O\), and insert \(y\) at any one of the
\(s\) positions of an ordered source upper tuple \(D\).  Use source
lower tuple \((C_0,t,\beta)\).  The promotion with departure \(x\) which
omits \(y\) has successor collar

\[
                         (A,t,\beta,U,B),
\]

lower block \(I-A\), and residual block \(O-B\).  It is exactly the
target (2.5).  If \(y\) is in position \(h\) of \(D\), its full collar
slot is

\[
                         j=H+d+h,qquad1\le h\le s.
\tag{3.1}
\]

At \(s=1\), take source lower tuple \((\beta)\), departure \(t\), and
source upper tuple \((y)\); omitting its last collar coordinate again
gives the native target in (2.7).  Therefore the unified promotion count
for one marked signature pair is

\[
 \boxed{
 P^{\rm ext}_{d,H}
 =s(m-d-2)_{s-1}(m-d-1)_{s-1}.}
\tag{3.2}
\]

### Theorem 3.1 (necessity of the trident normal form)

Let a coherent full state of a standard BTK radius-\(d\) chain have a
directed rotor successor which is a coherent state of a radius-\(d+1\)
BTK chain, with \(d<H\).  Then its two new target-free coordinates are
\((t,\beta)\), its fixed sets change as in (1.1), and its signatures have
exactly the form (0.1)--(0.3).

The same conclusion holds for a promotion whose omitted coordinate lies
in the source upper artificial tuple.  In that case the omitted coordinate
is \(y\).  A promotion omitting a source-native free coordinate, or a
source lower-artificial coordinate, cannot have a standard BTK
radius-\(d+1\) target.

#### Proof

Write a source collar as

\[
                         (C,U,D),\qquad |C|=|D|=s.
\]

After a rotor it is \((x,C,U,D^-)\).  A radius-\(d+1\) target has an
artificial prefix of length \(s-1\), followed by \(2d+2\) native free
coordinates.  If \(s\ge2\), direct position comparison forces

\[
 C=(C_0,t,\beta),\qquad A=(x,C_0),\qquad
 V_t=(t,\beta,U).
\tag{3.3}
\]

If \(s=1\), it instead forces \(C=(\beta)\), \(x=t\), and gives the same
target free word.  Equality of the lower and residual blocks then forces
one coordinate \(y\) to move from source fixed-out to target fixed-in and
forces exactly (1.1).  This is the rotor entry.

In the target signature, write the three Dyck gaps around its first two
free stars as \(P,R,S\).  Fixing \(t,\beta\) to one creates two excess
down-steps.  The change \(y:1\to0\) supplies exactly two excess up-steps.
If \(y\) were in \(R\), \(S\), or any later gap, the source prefix would
already fall below height zero at \(t\).  Hence \(P\ne\varnothing\) and
\(y\) is a closing letter in \(P\).  Section 1 proves that this condition
is also sufficient.

For a promotion deleting an upper-artificial coordinate, the same collar
position comparison gives (3.3).  Residual-block equality forces the
omitted coordinate to be the unique \(y\) in (1.1), giving the stated
promotion.

If an old free coordinate \(u_i\) is omitted, the target gap between its
two neighboring surviving free coordinates contains the newly fixed
letter \(1\) and otherwise only the two old Dyck gaps.  Its net height is
\(-1\), so it is not a Dyck gap.  If a lower-artificial coordinate is
omitted, the target frees one prefix coordinate and one post-\(U\)
coordinate; fixing them back in the source gives a terminal \(1\) in the
prefix before the first old free star with no compensating earlier change.
That source prefix has net height \(-1\).  Thus neither case is a BTK
signature pair. \(\square\)

### Theorem 3.2 (no upward jump larger than one)

Let \(0\le d<e\le H\), and put \(k=e-d\).  Suppose a coherent
radius-\(H\) state of a standard BTK radius-\(d\) chain has a
distinct-owner rotor or promotion successor which is coherent with a
standard BTK radius-\(e\) chain.  Then

\[
                         \boxed{k=1,}
\tag{3.4}
\]

and the transition is one of the tridents in Theorem 3.1.

#### Proof

Write the source collar as \((C,U,D)\), where

\[
 |C|=|D|=s=H-d,\qquad |U|=2d.
\]

The target has artificial prefix length \(s-k\).  After a rotor the
ordered collar is \((x,C,U,D^-)\).  Consequently the first \(k+1\)
coordinates in the target's native free word come from \(x,C\), and
hence all belong to the source native fixed-in set.  They precede every
coordinate of \(U\) in the target's increasing BTK free order.  The
rotor entry is the only coordinate which changes from source fixed-out
to target fixed-in.

Look at the target Dyck gaps before the first old free coordinate.  On
passing back to the source, the first \(k+1\) target stars become closing
letters \(1\).  To avoid falling below height zero at the first one, the
rotor entry must lie in the target's initial gap and changes there from
\(1\) to \(0\), supplying height exactly two.  All intervening target
gaps have net height zero.  The first two new closing letters use this
height, and a third would force height \(-1\).  Therefore \(k+1\le2\),
so \(k=1\).

For a distinct-owner promotion, the omitted slot must be greater than
\(H\); an earlier omission preserves the middle owner and cannot join
two different chains of one SCD.  The target native word again begins
with \(k+1\) source-fixed-in coordinates.  If the omitted coordinate is
source fixed-out, it is the unique possible \(0\to1\) change and the
same height argument applies.  If it is an old source free coordinate,
its collar index is greater than \(H\), so it lies in the latter half of
the increasing source free word.  A retained earlier source free
coordinate follows the \(k+1\) new target stars, while the omitted one
lies still later physically; it cannot repair the initial gap.  For
\(d=0\) there is no old free coordinate to omit.  Thus this case is
impossible, and again \(k=1\).

With \(k=1\), the position and fixed-set comparison is exactly that of
Theorem 3.1, which gives the trident normal form. \(\square\)

## 4. Exact chain counts

A radius-\(d+1\) signature is a sequence of \(2d+3\) Dyck gaps of total
semilength

\[
                         M=m-d-1.
\]

The initial gap is nonempty precisely for an eligible target.  Since
\(C(z)-1=zC(z)^2\),

\[
 \begin{aligned}
 E_d
 &=[z^M](C(z)-1)C(z)^{2d+2}\\
 &=[z^{M-1}]C(z)^{2d+4}\\
 &={d+2\over m}\binom{2m}{m-d-2}
 ={d+2\over m}N_{d+2}.
 \end{aligned}
\tag{4.1}
\]

Every signature has \(M\) matched pairs distributed symmetrically among
its \(2d+3\) gaps.  Therefore the total number of closing-coordinate
choices in the first gap is

\[
 {M\over2d+3}\gamma_{d+1}
 ={m-d-1\over m+d+2}N_{d+1}
 =N_{d+2}.
\tag{4.2}
\]

In particular, an eligible target has exactly

\[
                         {N_{d+2}\over E_d}={m\over d+2}
\tag{4.3}
\]

choices of \(y\) on average.  These many marked choices are not by
themselves an owner-disjoint matching.

Any trident matching at this boundary has the elementary capacity bound

\[
 |\mathcal M|\le\min\{\gamma_d,E_d\}.
\tag{4.4}
\]

Near the peak \(d\sim\sqrt{m/2}\), one has

\[
                         E_d=\left({1\over2}+o(1)\right)\gamma_{d+1}.
\tag{4.5}
\]

Thus the target eligibility cut alone permits at most half of the upper
peak layer.

## 5. An exact injective atomic-prefix bank

Restrict the target's first gap to

\[
                         P=(01)^k,\qquad k\ge1,
\tag{5.1}
\]

and choose \(y\) as its last letter.  Then the source first gap is

\[
                    (01)^{k-1}001R1S.
\tag{5.2}
\]

In the primitive-factor decomposition of (5.2), there are \(k-1\)
initial atomic factors \(01\), followed by the first non-atomic primitive
factor

\[
                         001R1.
\tag{5.3}
\]

Hence the source uniquely recovers \(k,y,t,\beta,R,S\) and the target.
The construction is owner-injective.  Moreover, every target first gap
in (5.1) has only atomic primitive factors, whereas every source first gap
has the non-atomic factor (5.3).  Thus source and target classes are
disjoint, even across adjacent radius boundaries.

The generating function for the nonempty atomic sequence (5.1) is
\(z/(1-z)\).  The other \(2d+2\) Dyck gaps are unrestricted, proving

\[
                         M_d
 =[z^{m-d-1}]{z\over1-z}C(z)^{2d+2}.
\tag{5.4}
\]

### Proposition 5.1 (peak density)

If \(d\sim\sqrt{m/2}\), then

\[
                         {M_d\over\gamma_{d+1}}\longrightarrow{1\over6}.
\tag{5.5}
\]

#### Proof

Write \(e=d+1\) and \(M=m-e\).  Expanding \(z/(1-z)\) gives

\[
 M_d=\sum_{k\ge1}[z^{M-k}]C(z)^{2e}.
\tag{5.6}
\]

The exact Lagrange formula

\[
 [z^j]C(z)^p={p\over2j+p}\binom{2j+p}{j}
\tag{5.7}
\]

shows, for each fixed \(k\), that

\[
 {[z^{M-k}]C(z)^{2e}\over[z^M]C(z)^{2e+1}}
 \longrightarrow {4^{-k}\over2}
\tag{5.8}
\]

when \(e\sim\sqrt{m/2}\).  The same exact binomial ratios bound the tail
uniformly by a geometric sequence, so dominated convergence applies to
(5.6).  Summing gives

\[
 {1\over2}\sum_{k\ge1}4^{-k}={1\over6}.
\]

The denominator in (5.8) is \(\gamma_e\), proving (5.5). \(\square\)

At a peak radius, \(\gamma_{d-1},\gamma_d,\gamma_{d+1}\) are
asymptotic.  Radius \(d\) chains used as incoming targets from boundary
\(d-1\to d\) have a purely atomic nonempty first gap.  Radius \(d\)
chains used as outgoing sources toward \(d+1\) have a first non-atomic
primitive factor.  These classes are disjoint.  Equations (5.5) at the
two adjacent boundaries therefore give

\[
 M_{d-1}+M_d
 =\left({1\over3}+o(1)\right)\gamma_d
\tag{5.9}
\]

incident radius-\(d\) chains, but no concatenation: the selected trident
bank is a vertex-disjoint matching.

## 6. The residual peak capacity cut

For a radius-\(d\) signature, classify its initial Dyck gap as follows:

* \(\mathcal E_d\): the gap is empty;
* \(\mathcal A_d\): it is a nonempty height-one word, equivalently
  \((01)^j\) with \(j\ge1\);
* \(\mathcal N_d\): it reaches height at least two.

Put \(e_d=|\mathcal E_d|\), \(a_d=|\mathcal A_d|\), and
\(n_d=|\mathcal N_d|\).  Also put

\[
 q_d=e_d+a_d
 =[z^{m-d}]{1\over1-z}C(z)^{2d}.
\tag{6.1}
\]

The first-gap-empty count is exact:

\[
 e_d=[z^{m-d}]C(z)^{2d}={d\over m}N_d.
\tag{6.2}
\]

Every upward trident has its source in \(\mathcal N_d\), because its
modified initial gap reaches height two, and has its target outside
\(\mathcal E_{d+1}\), because the closing coordinate \(y\) lies in a
nonempty initial gap.  Hence, in a directed path forest, the number
\(b_d\) of selected upward arcs across the two boundaries adjacent to
radius \(d\) satisfies

\[
 \boxed{
 b_d\le a_d+2n_d=2\gamma_d-q_d-e_d.}
\tag{6.3}
\]

Indeed, an empty-gap vertex supports no upward incidence, a height-one
vertex can only be an incoming target, and a height-at-least-two vertex
can support at most one incoming and one outgoing arc.

### Theorem 6.1 (global horizontal burden after all upward bridges)

Let \(F\) be a directed path forest on standard BTK chains, let \(p\)
be its component count, and let \(h_d\) count its selected arcs whose two
endpoints both have native radius \(d\).  Allow arbitrary downward
bridges and every coherent upward bridge.  Then

\[
 \boxed{
p+h_d\ge q_d+e_d-\gamma_d-N_{H+1}.}
\tag{6.4}
\]

If \(d\sim\sqrt{m/2}\) and
\(H=(1+o(1))\sqrt{m\log m}\) is calibrated so that
\(N_H=O(W/m)\), then

\[
 \boxed{
 q_d+e_d-\gamma_d-N_{H+1}
 =\left({1\over6}+o(1)\right)\gamma_d
 =\left({1\over6}\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
\tag{6.5}
\]

#### Proof

Let \(j_d\) count selected upward arcs crossing radius \(d\) whose target
has native radius greater than \(H\).  Distinct such arcs have distinct
targets, so the high-tail census gives

\[
                         j_d\le\sum_{r=H+1}^m\gamma_r=N_{H+1}.
\]

Delete these \(j_d\) arcs, the \(h_d\) horizontal radius-\(d\) arcs,
and the \(b_d\) upward arcs adjacent to radius \(d\).  Every other upward
arc crossing radius \(d\) has target radius at most \(H\), and Theorem
3.2 says that it is one of the deleted adjacent tridents.  Hence every
remaining path contains at most one radius-\(d\) chain.  Therefore

\[
                         p+h_d+b_d+j_d\ge\gamma_d.
\]

Combine this with (6.3) and \(j_d\le N_{H+1}\) to obtain (6.4).

It remains to evaluate the right side.  Equation (6.2) and the exact
formula

\[
 \gamma_d={2d+1\over m+d+1}N_d
\]

give \(e_d/\gamma_d\to1/2\) at the peak.  Write

\[
                         A_j=[z^j]C(z)^{2d}.
\]

Then \(q_d=\sum_{r=0}^{m-d}A_{m-d-r}\), and Lagrange inversion gives

\[
 {A_{j-1}\over A_j}
 ={j(j+2d)\over2(j+d-1)(2j+2d-1)}.
\tag{6.6}
\]

For every fixed \(r\), the product of the first \(r\) ratios in (6.6)
tends to \(4^{-r}\).  Uniformly while \(j\ge(m-d)/2\), the ratio is at
most \(1/3\) for all sufficiently large \(m\); the remaining tail is
exponentially smaller.  Hence

\[
                         {q_d\over e_d}\longrightarrow
                         \sum_{r\ge0}4^{-r}={4\over3}.
\tag{6.7}
\]

Thus \(q_d/\gamma_d\to2/3\).  At the calibrated height
\(H=(1+o(1))\sqrt{m\log m}\),

\[
 N_{H+1}=O(W/m)=o(\gamma_d),
\]

so (6.5) follows. \(\square\)

The theorem does not obstruct a standard-BTK construction with the
required number of same-radius bridges.  It allows arbitrary
exterior-moving jumps from below \(H\) to higher native radii, but their
entire target census contributes only the exact subtractive term
\(N_{H+1}\).  Radius-increasing transitions alone therefore cannot
supply the whole peak-crossing burden.

## 7. Exact boundary

Proved:

1. the trident signature is valid for every closing coordinate in a
   nonempty first Dyck gap;
2. its exact rotor collars, including the \(d=H-1\) departure correction;
3. its complete upper-deleting promotion family and exact slots;
4. the rotor/promotion necessity statement in Theorem 3.1;
5. the target, marked-pair, and extension-level counts;
6. the explicit atomic-prefix injective bank and its \(1/6\) peak density;
7. the disjoint incoming/outgoing \(1/3\)-incidence ledger;
8. impossibility of every upward jump larger than one; and
9. the global residual \((1/6+o(1))\gamma_d\) same-radius burden after
   all upward bridges, including jumps above \(H\), are admitted.

Not proved:

1. a matching saturating all eligible targets in (4.1);
2. a long alternating component system using non-atomic trident choices;
3. the required same-radius BTK bridge bank from Theorem 6.1;
4. simultaneous compatibility with the canonical last-free contraction;
   or
5. an \(o(W/H)\)-component path cover.

The trident mechanism therefore repairs the low-radius upward-bridge
failure of simple prefix unpairing, but its presently certified integral
bank is still component-short.
