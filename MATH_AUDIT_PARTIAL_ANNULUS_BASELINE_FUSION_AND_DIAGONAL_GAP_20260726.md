# Audit: the partial-annulus word, its missing baseline interface, and the diagonal gap

Date: 2026-07-26

## 0. Verdict

Put

\[
 n=2m,
 \qquad W=\binom{2m}{m},
 \qquad N_q=\binom{2m}{m-q}.
\]

The corrected partial-packet theorem is a valid standalone theorem for

\[
 \{m\}\cup\{m\pm q:q_0\le q\le H\}.
\]

It does **not** by itself cover the central ranks (1\le q<q_0).  Its
word already has length (W+o(W)), because the middle owners not used by
the packets are appended as middle-only singletons.  Concatenating a
separate (W+o(W)) PBBS central word therefore costs (2W+o(W)).

There are exactly two honest ways to remove this second baseline.

1.  Make the same packet family shallow-good as well.  The exact extra
    condition is derived in Section 1.  It is possible at the scalar
    level only when (q_0=o(m^{1/3})).
2.  Put the PBBS and packet witnesses into one common (W+o(W))-position
    word.  Section 3 states the exact order-and-cap/forbidden-interval
    condition for such a fusion.  At a fixed Gaussian entrance this must
    rewrite a positive fraction of the PBBS baseline; at a sub-Gaussian
    entrance it must rewrite (W-o(W)) positions.

Neither condition is presently proved.  In particular, a fixed-(a)
partial-annulus theorem cannot be turned into a full theorem merely by
writing (a=a_m\to0).

## 1. The exact missing shallow ledger

Let

\[
 K=\left\lfloor {N_{q_0}\over n}\right\rfloor,
 \qquad
 T=nK=N_{q_0}-\rho,
 \qquad 0\le\rho<n,
\tag{1.1}
\]

and select (K) cyclic packets.  For either sign
(sigma\in\{-,+\}), let (B_{q,S}^{\sigma}) be the load of the
rank-(q) target (S), and put

\[
 E_q^\sigma=\sum_S(B_{q,S}^{\sigma}-1)_+,
 \qquad
 M_q^\sigma=\#\{S:B_{q,S}^{\sigma}=0\}.
\tag{1.2}
\]

Every packet has exactly (n) starts at every depth, so

\[
 \sum_S B_{q,S}^{\sigma}=T.
\tag{1.3}
\]

If (D_q^\sigma) is the number of targets of positive load, then

\[
 D_q^\sigma=T-E_q^\sigma.
\]

Consequently, for **every** (q), including (q<q_0),

\[
 \boxed{
 M_q^\sigma=N_q-T+E_q^\sigma
 =N_q-N_{q_0}+\rho+E_q^\sigma.}
\tag{1.4}
\]

For (q\ge q_0), this is the forced-repeat identity already used in the
partial-annulus note.  For (q<q_0), all terms on the right are
nonnegative.  Hence the exact aggregate shallow-hole ledger is

\[
 \boxed{
 \sum_{q=1}^{q_0-1}\sum_{\sigma}M_q^\sigma
 =2\sum_{q=1}^{q_0-1}(N_q-N_{q_0}+\rho)
  +\sum_{q=1}^{q_0-1}\sum_\sigma E_q^\sigma.}
\tag{1.5}
\]

This identity separates the unavoidable occurrence deficit from the
actual cross-packet collisions.

### 1.1 Fixed Gaussian entrance

Let (q_0=a\sqrt m+O(1)), where (a>0) is fixed.  Uniform local
central-binomial asymptotics give

\[
 {N_q\over W}=e^{-q^2/m}+o_a(1)
 \qquad(0\le q\le q_0).
\]

Therefore the first term of (1.5) is

\[
 2W\sqrt m
 \left(\int_0^a e^{-x^2}\,dx-ae^{-a^2}\right)
 +o_a(W\sqrt m).
\tag{1.6}
\]

The bracket is strictly positive for (a>0), since its derivative is
(2a^2e^{-a^2}).  Thus even a completely collision-free selected packet
family has

\[
 \sum_{q<q_0,\sigma}M_q^\sigma=\Theta_a(W\sqrt m).
\tag{1.7}
\]

The fixed-(a) packet word therefore cannot cover or singleton-patch the
central band at coefficient one.  A shared baseline with PBBS, or another
correlated central compiler, is indispensable.

### 1.2 Moving entrance

Suppose (q_0\to\infty) and (q_0=o(\sqrt m)).  Uniformly for
(q\le q_0),

\[
 {N_q\over W}=1-{q^2\over m}
 +O\!\left({q_0^4\over m^2}+{q_0^2\over m^2}\right).
\tag{1.8}
\]

Summation yields

\[
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0}+\rho)
 =\left({4\over3}+o(1)\right){Wq_0^3\over m}.
\tag{1.9}
\]

The rounding contribution (2(q_0-1)\rho=O(mq_0)) is negligible
relative to (W).  Combining (1.5) and (1.9) gives the exact threshold:

\[
 \boxed{
 \sum_{q<q_0,\sigma}M_q^\sigma=o(W)
 \iff
 \left\{
 \begin{array}{l}
 q_0=o(m^{1/3}),\\[1mm]
 \displaystyle
 \sum_{q<q_0,\sigma}E_q^\sigma=o(W).
 \end{array}\right.}
\tag{1.10}
\]

Here the implication from left to right uses nonnegativity in (1.5), and
the reverse implication follows from (1.9).

Rank-(q_0) matching does not imply the second line of (1.10): two cyclic
orders may share a longer interval while their shorter rank-(q_0)
subintervals are different.  The hereditary identities in the packet
note run from (q_0) toward **larger** depths; they give no reverse
control at (q<q_0).

## 2. The corrected one-baseline packet reduction

The preceding calculation gives a complete conditional reduction which
does not mention PBBS.

### Theorem 2.1 (full-profile partial-packet compiler)

Let (H=O(\sqrt m)), let (q_0=o(m^{1/3})), and let
(mathcal F) consist of (K) packets as in (1.1).  Suppose

\[
 C_0(\mathcal F)=o(W),
\tag{2.1}
\]

\[
 \sum_{q=q_0}^{H}\sum_\sigma M_q^\sigma(\mathcal F)=o(W),
\tag{2.2}
\]

and

\[
 \sum_{q=1}^{q_0-1}\sum_\sigma E_q^\sigma(\mathcal F)=o(W).
\tag{2.3}
\]

Then one literal word covers the middle layer and every signed rank
(1\le q\le H), and has length (W+o(W)).

#### Proof

Use the packet word and append the omitted middle owners exactly as in
the corrected partial-annulus compiler.  Its length before target repair
is

\[
 W+C_0(\mathcal F)+2HK.
\]

Append each missing target through depth (H) once.  The annular repair
cost is (o(W)) by (2.2).  By (1.5), (1.9), and (2.3), the shallow repair
cost is also (o(W)).  Finally

\[
 2HK\le {H\over m}N_{q_0}=O(W/\sqrt m)=o(W).
\]

This proves the claim. \(\square\)

Thus a moving entrance can avoid PBBS, but only after proving a **uniform
full-profile packet theorem** down to (q_0=o(m^{1/3})).  The current
fixed-(a) theorem supplies neither the required rate nor (2.3).

There is one concrete structural way to make (2.3) automatic.  Fix an
SCD and retain its (N_{q_0}) chains of radius at least (q_0).  Assign the
packet starts injectively to all but (rho) of those chains.  If, for
every assigned start and every (q<q_0), its two signed packet traces are
the rank-(m-q) and rank-(m+q) members of the assigned SCD chain, then
the SCD partition property gives

\[
 E_q^-=E_q^+=0\qquad(q<q_0).
\tag{2.4}
\]

Thus an SCD-flag-coherent packet factor with (q_0=o(m^{1/3})) closes the
central interface by Theorem 2.1.  This is a useful exact alternative to
PBBS fusion.  It is not supplied by the present partial-annulus SCD
scaffold: that scaffold deliberately preserves the flags from (q_0)
outward while allowing the (2q_0) inner labels to be reordered.  Asking
for (2.4) spends precisely that inner-port freedom.

### 2.2 Why fixed-(a) diagonalization is insufficient

A statement proved separately for every fixed (a>0) normally supplies
an uncontrolled threshold (m\ge M(a)).  Standard diagonalization can
choose (a_m\to0), but only arbitrarily slowly.  Condition (1.10)
requires

\[
 a_m^3\sqrt m\to0,
 \qquad\hbox{equivalently}\qquad
 a_m=o(m^{-1/6}).
\tag{2.5}
\]

If the moving entrance is also required to satisfy (q_0\to\infty), the
full scalar window is

\[
 m^{-1/2}\ll a_m\ll m^{-1/6}.
\tag{2.6}
\]

No such rate follows from fixed-parameter convergence.  Moreover, even a
uniform theorem satisfying (2.5) would still need the shallow collision
condition (2.3).  Hence the phrase "take (a\to0) diagonally" does not
close the central interface.

If Theorem 2.1 could be proved for every fixed outer width
(H=b\sqrt m), with estimates that diagonalize in (b\to\infty), then
the usual exterior product-SCD tail would complete coefficient one.  This
is a valid full reduction, but it is substantially stronger than the
present fixed-annulus selection theorem.

### Corollary 2.2 (full reduction to coefficient one)

Assume that, for every fixed (b>0), there are packet families satisfying
Theorem 2.1 with (H=\lfloor b\sqrt m\rfloor), with normalized error
tending to zero, and with an entrance (q_0=q_0(m,b)) satisfying
(q_0=o(m^{1/3})).  Then the constant-one theorem follows.

Indeed, diagonalize over integer (b\to\infty), slowly enough that all
three normalized packet errors tend to zero and that (b=o(\sqrt m)).
Theorem 2.1 gives a word of length (W+o(W)) through the moving height
(H_m=b_m\sqrt m).  The audited product-SCD exterior beyond (H_m) has
length (o(W)) because (H_m/\sqrt m=b_m\to\infty).  Concatenating only
this exterior tail, rather than another baseline word, gives the full
constant-one construction.

## 3. Exact baseline sharing with PBBS

For a fixed Gaussian entrance, Section 1 rules out a standalone shallow
patch.  The PBBS and packet requirements must occupy essentially the same
baseline positions.

### 3.1 Atom-preserving form

Let (mathcal C) be the PBBS central template and (mathcal A) the
partial-packet template, including its omitted-owner singleton positions.
An atom-preserving fusion of length (L) is exactly the following
order-and-cap problem:

* embed the two atom sequences by increasing maps into ([L]);
* at each master position take the union of all embedded atoms; and
* whenever a master position lies between the embedded endpoints of a
  selected witness interval, require its master letter to be contained in
  that witness target.

The cap condition is what allows the foreign atoms between two packet or
PBBS atoms without enlarging their contiguous union.  A legal overlay
with (L=W+o(W)) gives one common baseline and proves the desired union
of the two coverage statements.  Merely identifying equal middle-owner
supports is not enough: chronology and every active cap must agree.

### 3.2 General wholesale rethreading form

There is an exact necessary-and-sufficient condition once witness
intervals have been scheduled.  Choose, in one line of length
(L=W+o(W)), intervals (I_\alpha) for

* all middle targets;
* all PBBS central targets, except an (o(W)) repair set; and
* all selected packet annulus targets, except an (o(W)) repair set,

with the packet intervals respecting their cyclic delay order.  For each
coordinate (x), define

\[
 F_x=\bigcup_{\alpha:x\notin S_\alpha}I_\alpha,
 \qquad A_x=[L]\setminus F_x.
\tag{3.1}
\]

Then nonempty letters realizing all prescribed unions exist if and only
if

\[
 x\in S_\alpha\Longrightarrow I_\alpha\cap A_x\ne\varnothing
\tag{3.2}
\]

for every (x,\alpha), and

\[
 \bigcup_xA_x=[L].
\tag{3.3}
\]

When these hold, the maximal realization is

\[
 Q_i=\{x:i\in A_x\}.
\tag{3.4}
\]

Equations (3.1)--(3.3), together with the PBBS and packet chronological
constraints on the scheduled intervals, are the exact general fusion
condition.  They make clear that the missing theorem is a global
endpoint-flag schedule, not a count of common middle supports.

### 3.3 Positive-density rewriting is necessary

In any word of length (W+e) covering the middle layer and rank
(m-q_0), at least (N_{q_0}-e) lower witnesses share a left endpoint
with a middle witness.  Thus a coefficient-one word must reuse
(N_{q_0}-o(W)) baseline endpoints.

If the PBBS central compiler is stopped immediately before (q_0), its
unchanged erosion letters have size strictly greater than (m-q_0).
The endpoint-capacity theorem therefore forces at least

\[
 N_{q_0}-o(W)
\tag{3.5}
\]

of those letters to be rewritten.  For (q_0=a\sqrt m), this is
((e^{-a^2}-o(1))W); for (q_0=o(\sqrt m)), it is (W-o(W)).

Consequently the selected packet supports cannot be inserted into the
existing PBBS compiler by collars, seams, or (o(W)) local edits.  A
successful fusion is necessarily the wholesale rethreading described by
(3.1)--(3.3).  The sparse morphological-preimage theorem proves that a
wholesale rewrite can preserve the middle layer and the upper PBBS tower,
but it does not yet preserve or reassign the lower central tower.

## 4. Audited boundary

Proved here:

1. the exact shallow load/hole identity (1.4);
2. the fixed-Gaussian unavoidable shallow deficit (1.6);
3. the sharp moving-entrance threshold (q_0=o(m^{1/3}));
4. the full-profile one-baseline reduction, Theorem 2.1;
5. the exact order-and-cap and coordinatewise forms of the PBBS/packet
   fusion gate; and
6. the positive-density/wholesale rewrite necessity.

Not proved:

1. the shallow packet collision estimate (2.3);
2. a packet selection theorem uniform down to (q_0=o(m^{1/3}));
3. a (W+o(W)) PBBS/packet legal overlay or wholesale endpoint schedule;
4. coefficient one.

The corrected conclusion is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{the partial-annulus theorem is a valid annular compiler, not yet a}
 \\
 \text{global coefficient-one reduction; its missing interface is either}
 \\
 \text{uniform shallow packet balance or a wholesale shared-baseline
 rethreading.}
 \end{gathered}}
\]
