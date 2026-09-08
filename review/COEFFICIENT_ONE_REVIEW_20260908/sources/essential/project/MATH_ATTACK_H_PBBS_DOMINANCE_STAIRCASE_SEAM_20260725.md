# Lane H: a linear PBBS crossing seam by a dominance staircase

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web search is used.

## 0. Verdict

The one-cut literal fusion problem has a linear solution.  Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}
\]

be a cyclic Johnson walk of rank \(m+1\), cut between \(X_{-1}\) and
\(X_0\).  If

\[
 2H\le m+1,
\tag{0.1}
\]

then one nonzero word of length

\[
 \boxed{4H-1}
\tag{0.2}
\]

represents every correct-rank lower intersection and every upper union of
at most \(H+1\) consecutive owners which crosses the cut.

The upper part is the literal owner segment of length \(2H\).  The lower
part has length \(2H-1\): attach to each coordinate its two positive-run
extents at the cut and follow a southeast lattice staircase through their
Pareto-minimal points.  Every correct lower target is the union of one
contiguous subpath of this staircase.

This is stronger than a zero-winding seam theorem: no PBBS return
classification is used.  In particular it is unaffected by the failure of
the proposed implication \(d(D)=1\Rightarrow g=2\operatorname{ht}(D)+1\)
recorded in `PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md`.

For completeness, that motivating converse fails literally at semilength
five.  With \(N=11\), put

\[
 D_0=1110011000,\qquad
 D_1=1110001100,\qquad
 D_2=1100111000.
\tag{0.3}
\]

Direct first-maximum factorization gives

\[
 \tau D_0=D_1,\quad \tau D_1=D_2,\quad \tau D_2=D_0,
\]

and

\[
 (\delta(D_0),d(D_0))=(3,1),\quad
 (\delta(D_1),d(D_1))=(3,5),\quad
 (\delta(D_2),d(D_2))=(7,1).
\tag{0.4}
\]

Although \(D_0\) is primitive, has height three, and has \(d(D_0)=1\),
its three-step-two deficit sum is

\[
 1+5+1=7\not\equiv3=\delta(D_0)\pmod {11}.
\tag{0.5}
\]

The earlier two sums are \(1\ne3\) and \(6\ne7\), so there is no claimed
gap-seven return.  The failed sector proof overlooks an old right-spine
forest after that forest is transported to positive depth on the left: its
relative height is below the global height, but relative height plus its
new attachment depth can attain the global height first.  Nothing below
uses the false iteration.

For \(J\) cuts on a cyclic owner component of length \(\ell\), the exact
endpoint-erosion plus seam cost is

\[
 \boxed{\ell+(5H-1)J.}
\tag{0.6}
\]

Thus the old \(\Theta(H^2)\) singleton-repair toll per cut is removed.
The fixed-window packing statement \((RP_A)\) remains neither proved nor
disproved.  The linear seam nevertheless weakens the sufficient residence
hypothesis from little-oh Catalan packing to big-oh Catalan packing.  This
is proved in Section 9.  If instead a regime contains \(\Theta(W/H)\)
essential cuts, paying \(\Theta(H)\) independently at all of them is still
\(\Theta(W)\); there the surviving fallback is genuine cross-cut chart
sharing.

## 1. The crossing Pascal triangle

Put

\[
 C=X_{-1}\cap X_0.
\tag{1.1}
\]

Because the two owners are adjacent rank-\((m+1)\) sets,

\[
 |C|=m.
\tag{1.2}
\]

For \(1\le s,t\le H\), define

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.
\tag{1.3}
\]

This window contains \(s+t\) owners and \(s+t-1\) Johnson transitions.
Its floor rank is therefore

\[
 m+1-(s+t-1)=m+2-s-t.
\tag{1.4}
\]

We call \(P_{s,t}\) **floor-correct** when equality holds:

\[
 |P_{s,t}|=m+2-s-t.
\tag{1.5}
\]

Every intended correct lower mask crossing the cut and using at most
\(H+1\) owners is one of these queries, with

\[
 s+t-1\le H.
\tag{1.6}
\]

It is convenient, and costs nothing, to construct the chart for the whole
square \([H]^2\).

For \(x\in C\), define its capped left and right positive-run extents by

\[
 u_x=\max\{u\in[H]:x\in X_{-u}\cap\cdots\cap X_{-1}\},
\tag{1.7}
\]

\[
 v_x=\max\{v\in[H]:x\in X_0\cap\cdots\cap X_{v-1}\}.
\tag{1.8}
\]

Write

\[
 p_x=(u_x,v_x),\qquad
 \mathcal D=\{p_x:x\in C\}\subseteq[H]^2,
\tag{1.9}
\]

with multiplicities allowed.

### Lemma 1.1 (dominance formula)

For every \((s,t)\in[H]^2\),

\[
 \boxed{P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.}
\tag{1.10}
\]

#### Proof

The defining owner window contains \(X_{-1}\) and \(X_0\), so its
intersection is contained in \(C\).  A coordinate of \(C\) survives the
whole window precisely when its positive run through the cut reaches at
least \(s\) owners leftward and at least \(t\) owners rightward.  This is
exactly (1.10). \(\square\)

For \(s,t<H\), put

\[
 R_{s,t}=P_{s,t}\setminus(P_{s+1,t}\cup P_{s,t+1}).
\tag{1.11}
\]

By (1.10), \(R_{s,t}\) consists exactly of the coordinates with
\((u_x,v_x)=(s,t)\).  Hence the literal Pascal recurrence is

\[
 \boxed{P_{s,t}=P_{s+1,t}\cup R_{s,t}\cup P_{s,t+1}.}
\tag{1.12}
\]

The nonempty \(R_{s,t}\)'s are precisely the short-run pins which make
independent repair of all triangle cells quadratic.

## 2. Floor correctness gives southwest exclusion

### Lemma 2.1

If \(P_{s,t}\) is floor-correct, no extent point lies strictly southwest
of \((s,t)\):

\[
 \boxed{
 \nexists x\in C\quad u_x<s\text{ and }v_x<t.}
\tag{2.1}
\]

#### Proof

List the \(L=s+t\) owners in (1.3) as

\[
 Y_0=X_{-s},Y_1,\ldots,Y_{L-1}=X_{t-1}.
\]

For each coordinate of \(Y_0\) missing from the total intersection, mark
the transition at which it first departs.  Different initial coordinates
have different marked transitions, because a Johnson transition departs
only one coordinate.  Thus this is an injection from
\(Y_0\setminus P_{s,t}\) into the \(L-1\) internal transitions.

Suppose \(x\in C\) satisfies \(u_x<s\) and \(v_x<t\).  The first
inequality means that \(x\) is absent somewhere on the left of its
positive run through the cut, so \(x\) has an internal arrival.  The
second means that it later has an internal departure on the right.

That later departure transition is not the first-departure image of any
initial coordinate.  If \(x\notin Y_0\), then \(x\) is not initial.  If
\(x\in Y_0\), it already departed before the internal arrival, so the
later departure is not its first departure.  Since the transition departs
\(x\), it cannot be the marked first departure of another coordinate.

At most \(L-2\) transitions are therefore used by the injection.  Hence

\[
 |P_{s,t}|
 =|Y_0|-|Y_0\setminus P_{s,t}|
 \ge(m+1)-(L-2)
 =m+3-s-t,
\]

contradicting (1.5). \(\square\)

The strict inequalities in (2.1) matter.  Extent points directly west,
directly south, or northeast of a correct query are allowed.

## 3. The Pareto staircase

Discard multiplicities in \(\mathcal D\), take its Pareto-minimal points,
and list them as

\[
 d_1=(a_1,b_1),\ldots,d_r=(a_r,b_r)
\tag{3.1}
\]

with increasing first coordinate.  Their second coordinates strictly
decrease.

Construct a southeast unit lattice path \(\Gamma\) from \((1,H)\) to
\((H,1)\) through \(d_1,\ldots,d_r\).  On the initial segment, between
successive minima, and on the final segment, move east first and then
south.  The path makes \(H-1\) east and \(H-1\) south steps, so

\[
 \boxed{|V(\Gamma)|=2H-1.}
\tag{3.2}
\]

### Lemma 3.1 (rectangle interception)

Let \(q\in[H]^2\) have no point of \(\mathcal D\) strictly southwest of
it.  If \(p\in\mathcal D\) and \(p\ge q\), then

\[
 \boxed{V(\Gamma)\cap[q,p]\ne\varnothing.}
\tag{3.3}
\]

#### Proof

Choose a Pareto-minimal point \(d\in\mathcal D\) with \(d\le p\).
Such a point is obtained by descending inside the finite set
\(\mathcal D\cap(-\infty,p]\).

If \(d\ge q\), use \(d\).  The forbidden southwest case leaves two
possibilities.

If \(d_1<q_1\) and \(d_2\ge q_2\), follow \(\Gamma\) forward.  Before
its first coordinate reaches \(q_1\), no Pareto minimum can have second
coordinate below \(q_2\), since that would be a point strictly southwest
of \(q\).  The east-before-south convention therefore supplies a vertex

\[
 z=(q_1,z_2),\qquad z_2\ge q_2.
\]

Forward motion from \(d\) never raises the second coordinate, so
\(z_2\le d_2\le p_2\), and clearly \(z_1=q_1\le p_1\).  Thus
\(q\le z\le p\).

If \(d_1\ge q_1\) and \(d_2<q_2\), follow the path backward.  Backward
motion goes north before west.  Until height \(q_2\) is reached, every
Pareto minimum has first coordinate at least \(q_1\), again by southwest
exclusion.  Hence there is a vertex

\[
 z=(z_1,q_2),\qquad z_1\ge q_1.
\]

Backward motion from \(d\) never raises the first coordinate, so
\(z_1\le d_1\le p_1\), while \(z_2=q_2\le p_2\).  Thus
\(q\le z\le p\) in this case as well.  The same argument includes the
initial and terminal endpoint segments of \(\Gamma\). \(\square\)

## 4. The linear lower word

For each staircase vertex \(z=(s,t)\), use the actual set-letter

\[
 W_z=P_{s,t}.
\tag{4.1}
\]

Emit these \(2H-1\) letters in their order along \(\Gamma\).

### Theorem 4.1 (literal lower staircase identity)

For every floor-correct query \(q=(s,t)\),

\[
 \boxed{
 P_{s,t}
 =\bigcup_{\substack{z\in V(\Gamma)\\ z\ge(s,t)}}W_z.}
\tag{4.2}
\]

The letters on the right form one contiguous subword.  Every emitted
letter is nonzero.

#### Proof

Along \(\Gamma\), the first coordinate is nondecreasing and the second is
nonincreasing.  Thus the condition \(z_1\ge s\) selects a suffix and
\(z_2\ge t\) a prefix; their intersection is a contiguous subpath.

If \(z\ge(s,t)\), (1.10) gives \(W_z\subseteq P_{s,t}\).  Conversely,
take \(x\in P_{s,t}\).  Then \(p_x\ge(s,t)\).  Lemma 2.1 gives the
southwest-exclusion hypothesis of Lemma 3.1, so there is

\[
 z\in V(\Gamma)\cap[(s,t),p_x].
\]

Since \(p_x\ge z\), (1.10) gives \(x\in W_z\).  This proves (4.2).

Finally, \(W_z=P_{s,t}\) intersects \(s+t\le2H\) consecutive owners.
At most one initial coordinate is lost at each of the \(s+t-1\)
transitions, so

\[
 |W_z|\ge m+2-s-t\ge m+2-2H\ge1
\]

by (0.1). \(\square\)

## 5. The upper word and exact one-cut length

Emit the owner segment

\[
 W^+=X_{-H},X_{-H+1},\ldots,X_{H-1}.
\tag{5.1}
\]

Every upper union of at most \(H+1\) consecutive owners crossing the cut
is exactly the union of its corresponding contiguous subsegment of
\(W^+\).  These \(2H\) owner letters are nonzero.

Concatenate the lower staircase word and \(W^+\).  All chosen witnesses
stay inside their own block, so no compatibility condition is introduced
at the concatenation.  The total length is

\[
 \boxed{(2H-1)+2H=4H-1.}
\tag{5.2}
\]

This proves (0.2), with every target witnessed by a literal contiguous OR.

## 6. Several cuts

Consider a cyclic projected-owner component of length \(\ell\), and cut
it at \(J\ge1\) transition edges meeting every positive residence of
length at most \(H\).  Endpoint-capped erosion of the resulting \(J\)
paths uses

\[
 \ell+HJ
\tag{6.1}
\]

letters and preserves every correct target whose owner window remains
inside a path.

Append the \((4H-1)\)-letter chart at every cut.  If a depth-at-most-\(H\)
window crosses several nearby cuts, choose any one of them.  Relative to
that cut the window uses \(s,t\ge1\) and satisfies \(s+t-1\le H\), and
the chart is defined from the original cyclic owners, not from unrelated
endpoint dummies.  Hence it represents the window exactly.

The total component length is

\[
 \ell+HJ+(4H-1)J
 =\boxed{\ell+(5H-1)J}. 
\tag{6.2}
\]

Projected PBBS owner cycles have length at least \(2m+1\).  Under (0.1),
all indices in each \(2H\)-owner chart therefore lie in one unambiguous
cyclic neighborhood.

There is an exact source of sharing which the additive bound (6.2) ignores.
If the cut is between \(X_{c-1}\) and \(X_c\), write

\[
 P^{(c)}_{s,t}=\bigcap_{i=c-s}^{c+t-1}X_i.
\tag{6.3}
\]

Then adjacent cuts satisfy the literal diagonal identity

\[
 \boxed{
 P^{(c)}_{s,t}=P^{(c+1)}_{s+1,t-1}}
\tag{6.4}
\]

whenever \(1\le s,t\le H\), \(t\ge2\), and \(s+1\le H\).  Both sides
are the intersection over the same global owner interval.  More generally,
two cells at two cuts are identical whenever their global left and right
endpoints agree.

Thus a bulk construction should place all selected cuts in the global
endpoint plane and share repeated staircase cells there.  Merely appending
the local paths discards this exact equality.  Identity (6.4) alone does
not give a sublinear global bound when successive selected cuts are
typically \(\Theta(H)\) apart, but it identifies the correct object for the
next fusion step.

## 7. Linear order is unavoidable

### Proposition 7.1

Suppose one cut has \(t\) distinct crossing targets of one common rank.
Every literal word which represents all of them has length at least \(t\).
Consequently a strong depth-\(H\) Johnson collar, whose \(H\) crossing
upper targets are distinct and have one rank, requires at least \(H\)
letters in any seam chart.

#### Proof

Choose one witnessing interval for each target.  If two chosen intervals
have the same left endpoint, one contains the other.  Their ORs are then
comparable by inclusion.  Distinct sets of the same cardinality are
incomparable, so this is impossible.  Thus the \(t\) witnesses have
distinct left endpoints, and a word containing them has at least \(t\)
positions. \(\square\)

Hence the \(4H-1\) construction has optimal order of growth.  This lower
bound does not assert that its constant four is sharp.

The following explicit collar strengthens the constant in this order
lower bound for the full arbitrary-Johnson scope.

### Proposition 7.2 (explicit triangular counting lower bound)

Assume \(2H\le m+1\).  There is a rank-\((m+1)\) Johnson collar for which
all

\[
 \frac{H(H+1)}2
\]

required lower crossing targets are floor-correct and distinct, and the
same is true of the upper targets.  Any word covering just the lower
triangle has length at least \(H\); any word covering both triangles has
length at least

\[
 \boxed{
 \left\lceil\frac{\sqrt{1+8H(H+1)}-1}{2}\right\rceil
 = (\sqrt{2}+o(1))H.}
\tag{7.1}
\]

#### Proof

Choose pairwise disjoint sets

\[
 K,\quad A=\{\alpha_1,\ldots,\alpha_{H-1}\},\quad
 B=\{\beta_1,\ldots,\beta_{H-1}\},
\]

\[
 L=\{\ell_0,\ldots,\ell_{H-1}\},\quad
 R=\{\rho_0,\ldots,\rho_{H-1}\},
\]

with \(|K|=m-2H+2\).  They use \(m+2H\le2m+1\) coordinates.  For
\(1\le s,t\le H\), define

\[
 X_{-s}
 =K\cup B\cup\{\alpha_u:u\ge s\}
       \cup\{\ell_0,\ldots,\ell_{s-1}\},
\tag{7.2}
\]

\[
 X_{t-1}
 =K\cup A\cup\{\beta_v:v\ge t\}
       \cup\{\rho_0,\ldots,\rho_{t-1}\}.
\tag{7.3}
\]

Every owner has size \(m+1\).  Consecutive negative-side owners exchange
\(\ell_{s-1}\) for \(\alpha_{s-1}\), consecutive positive-side owners
exchange \(\beta_t\) for \(\rho_t\), and the cut exchanges \(\ell_0\)
for \(\rho_0\).  Thus this is a literal Johnson collar.

Direct intersection and union give

\[
 P_{s,t}
 =K\cup\{\alpha_u:u\ge s\}
       \cup\{\beta_v:v\ge t\},
\tag{7.4}
\]

\[
 U_{s,t}
 =(K\cup A\cup B)
   \cup\{\ell_0,\ldots,\ell_{s-1}\}
   \cup\{\rho_0,\ldots,\rho_{t-1}\}.
\tag{7.5}
\]

Hence

\[
 |P_{s,t}|=m+2-s-t,\qquad |U_{s,t}|=m+s+t,
\]

and both indexed families are injective.  Restricting to
\(s,t\ge1\), \(s+t-1\le H\), gives \(H(H+1)/2\) lower targets and the
same number of upper targets.  The two families are disjoint by
cardinality.

A word of length \(n\) has only \(n(n+1)/2\) nonempty intervals, hence at
most that many distinct interval-OR outcomes.  The lower family alone
forces

\[
 \frac{n(n+1)}2\ge\frac{H(H+1)}2,
\]

so \(n\ge H\).  Both families together force

\[
 \frac{n(n+1)}2\ge H(H+1),
\]

which is (7.1). \(\square\)

This construction proves order optimality for the theorem's arbitrary
Johnson-cut domain.  It is not asserted that this exact collar occurs at
every PBBS cut.

## 8. Exact scope and adversarial audit

1. The construction is integral and factor-native.  Every helper letter is
   an actual owner intersection, and every upper helper is an actual owner.
2. Floor correctness is essential.  Lemma 2.1 need not hold for an
   oversized intersection, and the theorem makes no claim for one.
3. The east-before-south corner convention is essential in the two
   one-sided cases of Lemma 3.1.
4. The constants \(4H-1\) and \(5H-1\) are exact for this construction.
5. No FIFO, LIFO, zero-winding, primitive-root, or endpoint-order
   hypothesis is used.  The known local endpoint permutation \(213\) is
   therefore harmless.
6. The theorem solves sharing among the \(\Theta(H^2)\) targets destroyed
   at one cut.  It does not share the \(\Theta(H)\)-letter charts belonging
   to different cuts.

Consequently, in a dense-residence regime with \(J=\Theta(W/H)\), the
local theorem alone still pays \(\Theta(W)\).  The smallest remaining
fusion statement is:

> Given the actual family of selected PBBS cuts, merge their dominance
> staircases in the global endpoint plane and merge their owner charts into
> total added length \(o(HJ)\), while
> retaining one literal contiguous witness for every correct crossing
> target and the endpoint-capped internal targets.

That is a cross-cut sharing problem.  The quadratic one-cut Pascal toll is
no longer part of the obstruction.

## 9. Conditional coefficient-one theorem with the weakened packing gate

Let

\[
 B_m=\operatorname{Cat}_m=\frac{W}{2m+1}.
\]

Here \(\nu_H(P_m)\) is the full-deck complement-projected residence
packing number, exactly as in Section 22 of the residence reduction; it is
the sum of the packing numbers of the physical owner cycles, not the
quotient packing
\(\overline\nu_H\).

For every active projected cycle \(C\), choose a minimum transversal of its
residence intervals of length at most \(H\).  If \(J_C\) is its size, the
circular interval packing--transversal theorem gives

\[
 J_C\le\nu_H(C)+1\le2\nu_H(C),
\tag{9.1}
\]

because an active cycle has \(\nu_H(C)\ge1\).  Inactive cycles use their
cyclic erosion words, at overhead \(2H\) each.  The number of projected
cycles is at most \(B_m\).  Summing (6.2) therefore gives the explicit
deterministic upper ledger

\[
 \boxed{
 L_H\le
 W+2HB_m+2(5H-1)\nu_H(P_m).}
\tag{9.2}
\]

### Theorem 9.1 (Catalan-order residence packing suffices)

Assume that for every fixed \(A>0\), with

\[
 H_A=\lceil A\sqrt m\rceil,
\]

one has

\[
 \boxed{\nu_{H_A}(P_m)=O_A(B_m).}
\tag{CP_A}
\]

Then

\[
 \boxed{
 \nu(k)\le(1+o(1))
 \binom{k}{\lfloor k/2\rfloor}.}
\tag{9.3}
\]

#### Proof

For fixed \(A\), let \(K_A<\infty\) be a constant in \((CP_A)\).  At
\(H=H_A\), (9.2) gives

\[
 \frac{L_H-W}{W}
 \le
 \frac{2H+2K_A(5H-1)}{2m+1}
 =O_{A,K_A}(m^{-1/2})=o_A(1).
\tag{9.4}
\]

Thus the complete audited PBBS support in every fixed Gaussian central
window has one literal word of length \(W+o_A(W)\).

For completeness, diagonalize without requiring uniformity in \(A\).
For each integer \(j\ge1\), choose a valid constant \(K_j\) and then,
recursively, an increasing threshold \(M_j\) so large that, for every
\(m\ge M_j\),

\[
 \nu_{\lceil j\sqrt m\rceil}(P_m)\le K_jB_m,
 \qquad
 \frac{j(1+K_j)}{\sqrt m}\le\frac1j,
 \qquad 2\lceil j\sqrt m\rceil\le m+1,
 \qquad m\ge j^{12}.
\tag{9.5}
\]

The audited product-SCD tail theorem gives, for fixed \(j\), normalized
tail cost

\[
 O\!\left((1+j^2)e^{-j^2+o_m(1)}\right).
\tag{9.6}
\]

Increase \(M_j\) so that this cost is at most
\(\eta_j=C(1+j^2)e^{-j^2/2}\), for one absolute \(C\); then
\(\eta_j\to0\).  Define \(a(m)=j\) on
\(M_j\le m<M_{j+1}\) and put

\[
 H_m=\lceil a(m)\sqrt m\rceil.
\]

Then \(a(m)\to\infty\), \(H_m=o(m)\), the central excess in (9.2) is
\(o(W)\) by (9.5), and the outer-tail word also has length \(o(W)\).
This proves (9.3) in odd dimension.  The audited trimmed one-coordinate
lift gives the same leading constant in even dimension. \(\square\)

The hypothesis \((CP_A)\) is strictly weaker than \((RP_A)\), but it is
still unproved; what was retracted is the claimed disproof of \((RP_A)\).
The linear seam closes the literal
quadratic repair loss; the remaining positive gate is now Catalan-order,
chronology-sensitive residence packing, or an even stronger cross-cut
fusion which avoids paying (9.2) independently.

For fixed \(A\), the deck reduction makes this gate equivalently

\[
 \boxed{
 \overline\nu_{H_A}=O_A\!\left(\frac{B_m}{2m+1}\right).}
\tag{9.7}
\]

Indeed,

\[
 (2m+1)\overline\nu_H
 \le\nu_H(P_m)
 \le2(2m+1)\overline\nu_H+(2m+1)Z_H,
\]

and \((2m+1)Z_H=o(B_m)\) throughout every fixed Gaussian window.  Thus
the exact remaining packing scale is big-oh \(B_m/(2m+1)\), rather than
the little-oh quotient scale forced by singleton seam repair.
