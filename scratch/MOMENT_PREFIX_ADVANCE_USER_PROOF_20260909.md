# Height-moment prefixes: a uniform ten-parts-per-million bound

## Status and scope

This is a further **conditional, computer-assisted** estimate for the same
height-adaptive interval-union word. It retains the finite strict-height
matching-corridor construction, equality-particle reduction, inverse-pruning
fibre and exact period criterion specified in `PREFIX_PERIOD_BOUND.md` and
`EXACT_PERIOD_CENSUS.md`. It does not independently certify those inherited
premises. The original manuscript describes its reviews as internal rather than
external or formal. This continuation is not a proof-assistant certificate or an
independent external review of that manuscript.

No asymptotic concentration, critical-size probability mixture, logarithmic-gcd
sieve or renewal theorem is needed here. No finite word, including the separately
reported dimension-17 word, has been altered or reverified. No new optimality
claim for the extremal quantity nu(k) is made.

The new ingredients are exact conditional HEIGHT TOTALS for an unfinished
pruning core; a primitive-row baseline with a rigorously charged symmetry
correction; and sparse child expansion with an explicit residual-mass charge.
All unfinished families remain accounted for.

## 1. Result

Let nu(k) denote the least length of a word of nonempty subsets of [k] whose
nonempty, contiguous, nonwrapping interval unions contain every nonempty subset.
Let W(k)=binom(k,floor(k/2)). On the stated finite inputs, the certificates and
analytic argument below give

\[
 \boxed{\nu(k)<(1+10^{-5})W(k)\qquad\text{for every integer }k\ge137.} \tag{T1}
\]

The previously supplied uniform sufficient threshold at this precision was 6849.
The new threshold is attained for the unchanged height-adaptive constructor and
its prescribed odd-to-even lift: that constructor fails this tolerance at
both dimensions 135 and 136. This is NOT a lower bound ruling out different,
better words at those dimensions.

The earlier 1/1000 and 1/10000 guarantees, starting at dimensions 57 and 87,
remain valid. The earlier conditional eventual stretched-exponential estimate
also remains a separate result on its stated premises; its exponent is not
improved or independently recertified here.

The exact endpoint-count lower bound B(k)<=nu(k), with B(k)>=W(k), gives

\[
 0\le\nu(k)-B(k)<10^{-5}W(k)\qquad(k\ge137). \tag{T2}
\]

The finite calculation establishes every case r=68,...,3423. A separately
proved decreasing analytic envelope covers every r>=3424. Both parts are
required for the word "every" in T1.

## 2. Retained finite construction and period bounds

In odd dimension n=2r+1, put W_r=binom(2r+1,r)=n Cat_r. The height-adaptive
construction has exact length

\[
 N_r=W_r+\sum_{\mathcal C}(2h_{\mathcal C}-1),\qquad
 \frac{N_r-W_r}{W_r}
 =\frac1{\operatorname{Cat}_r}\sum_{|D|=r}\frac{2h(D)-1}{v(D)}. \tag{2.1}
\]

The sum on the right is over rooted Dyck words, not uniformly chosen cycles.
Here h is the invariant height and v is the full cycle period of the squared
parenthesis-flip map. The inherited strict-height corridor establishes full-cube
coverage, and all emitted letters and witnesses are nonempty. Also n divides v.

Write a_s for the original pruning semilength, n_s=2a_s+1, and d_s for the least
cyclic period of row s, whose length is n_(s+1). For a full return, the exact
forward recurrence from the preceding note is

\[
 \beta_0=0,\qquad
 \beta_{s+1}=\frac{1+n_{s+1}\beta_s}{n_s},\qquad
 v=\operatorname{lcm}_{s<h}\operatorname{den}(\beta_{s+1}/d_s). \tag{2.2}
\]

Thus a specified prefix supplies a period divisor P for EVERY completion. If
its next two sizes are a=a_s and b=a_(s+1), let

\[
 \beta'=\frac{1+(2b+1)\beta_s}{2a+1},\qquad
 P_d=\operatorname{lcm}\{P,\operatorname{den}(\beta'/d)\}. \tag{2.3}
\]

For a completion whose current row has least period d, P_d divides its full
period. Put p=2b+1. Since d divides p, P_d divides P_p. Nonprimitive rows are
not assumed absent.

The exact Narayana count is

\[
 K(a,b)=\frac1a\binom ab\binom a{b+1},\qquad 0\le b<a. \tag{2.4}
\]

It counts size-a Dyck roots whose first pruned size is b. For b>0 the next size
c ranges over max(0,2b-a)<=c<=b-1, and the row fibre has cardinality
binom(a+c,2b). In particular

\[
 K(a,b)=\sum_c\binom{a+c}{2b}K(b,c). \tag{2.5}
\]

Let C(p,ell;d) count ORDERED length-p composition rows of mass ell and least
cyclic period d. It is zero unless d|p and e=p/d divides ell. Otherwise, with
m=ell/e,

\[
 C(p,\ell;d)=\sum_{j\mid\gcd(d,m)}\mu(j)
                    \binom{(d+m)/j-1}{d/j-1}. \tag{2.6}
\]

These are ordered-row counts, not necklace counts. Summing in d gives the
complete weak-composition fibre. These finite inputs are exactly the ones in
the preceding period-prefix work.

## 3. New exact height-total recurrence

Define

\[
 H(a,b)=\sum_{\substack{|D|=a\\|\partial D|=b}}h(D). \tag{3.1}
\]

This is an integer TOTAL, not a conditional mean approximation. For b=0 there
is one root, (10)^a, of height one. Therefore H(a,0)=1.

For b>0,

\[
 \boxed{H(a,b)=K(a,b)+
       \sum_{c=\max(0,2b-a)}^{b-1}\binom{a+c}{2b}H(b,c).} \tag{3.2}
\]

**Proof.** Each remaining core E with sizes (b,c) has exactly binom(a+c,2b)
preimages in the fibre. Each such parent has height h(E)+1: simultaneously
removing all peaks lowers the nonzero height by exactly one. Sum h(E)+1 over
all cores and fibres and apply (2.5). No independence between height and
period is required. QED.

The recurrence is triangular in a, so any finite table can be computed by exact
integer arithmetic. An implementation should use the adjacent-binomial ratio
rather than recompute every binomial coefficient.

For example, the conditional mean H(100,50)/K(100,50) is approximately
16.42824502, whereas the preceding prefix cap was 51 for every member of that
same family. The calculation uses the exact integer numerator and denominator;
the decimal is only illustrative.

### 3.1 New moment bound for any unfinished prefix

Suppose a prefix has reached sizes (a,b) at level s, has upper-row multiplicity
w and period divisor P. Its completions have original height s+h(D), and there
are w K(a,b) completions. Thus its contribution to the unnormalized sum in
(2.1) is at most

\[
 \boxed{\frac{w\{(2s-1)K(a,b)+2H(a,b)\}}{P}.} \tag{3.3}
\]

The old contribution was w K(a,b)(2s+2b+1)/P. Since h(D)<=b+1, (3.3) is never
larger. It is often strictly smaller. The argument uses a constant period
LOWER BOUND across the family, so it does not factor a correlated expectation.

## 4. A cheap finite substitute for a large height table

The actual implementation evaluates H exactly when a<=250. For larger a, the
following elementary bound avoids a large table. It is a bound for EVERY
subset of K size-a Dyck roots, not just a peak-conditioned class.

Let the canonical height be h. Lift each rooted Dyck word to its 2a+1 distinct
rotations on the middle layer. For any fixed linear cut, let M and m be the
maximum and minimum partial sums of the bridge, including its endpoints. Then
h<=M-m. For any integer t>=0,

\[
 (h-2t)_+\le(M-t)_++(-m-t)_+.
\]

The elementary reflection counts are

\[
 \#\{M\ge j\}=\binom{2a+1}{a-j},\qquad
 \#\{-m\ge j\}=\binom{2a+1}{a+1-j}.
\]

If 0<=t<a and j=a-t, put

\[
 B_a(t)=\frac1{2a+1}
 \left\{\sum_{i=0}^{j-1}\binom{2a+1}{i}
       +\sum_{i=0}^{j}\binom{2a+1}{i}\right\}. \tag{4.1}
\]

For any such K-root subfamily, including the class in (3.1),

\[
 \boxed{\sum h(D)\le2tK+B_a(t).} \tag{4.2}
\]

Indeed, sum (h-2t)_+ over all roots, bound by the bridge excess over all rotations,
and divide by 2a+1. This pays for the whole omitted positive part.

For quick exact computation the two binomial tails are bounded geometrically:

\[
 B_a(t)\le G_a(t):=
 \frac{\binom{2a+1}{a-t}}{2a+1}
 \left\{\frac{a+t+2}{2t+2}
       +\frac{(a-t)(a+t+3)}{(a+t+2)(2t+4)}\right\}. \tag{4.3}
\]

For example, for j<n/2, the ratios in the lower binomial tail are at most
j/(n-j+1), proving sum_(i<=j) binom(n,i)<=binom(n,j)(n-j+1)/(n-2j+1).
Apply this at j and j-1. All quantities in (4.3) are rational.

The implementation sets K=K(a,b), chooses q as the least nonnegative integer
with 2^q K>=Cat_a, and chooses t=floor(sqrt((a+1)(q+2)))+1. ANY t is permitted;
this choice is an efficiency heuristic, not a premise. Define

\[
 \widehat H(a,b)=\min\{(b+1)K(a,b),\;2tK(a,b)+\lceil G_a(t)\rceil\}. \tag{4.4}
\]

If t>=a, the deterministic cap alone is sufficient. At a<=250 use the exact
H(a,b) instead. In all cases H<=Hhat<=(b+1)K.

## 5. Integrate the next period constraint before exposing its next size

For fixed a,b and a row period d|p, define

\[
 M_d(a,b)=\sum_c C(p,a-2b+c;d)K(b,c),
\qquad
 R_d(a,b)=\sum_c C(p,a-2b+c;d)H(b,c). \tag{5.1}
\]

The original-height weight of this class is

\[
 A_d=w\{(2s+1)M_d+2R_d\}.
\]

Since its period is at least P_d, a valid one-row-integrated charge is

\[
 \sum_{d\mid p}\frac{A_d}{P_d}. \tag{5.2}
\]

Because every P_d divides P_p, this has the useful exact decomposition

\[
 \boxed{
 \frac{w\{(2s-1)K+2H\}}{P_p}
 +w\sum_{d<p}\{(2s+1)M_d+2R_d\}
          \left(\frac1{P_d}-\frac1{P_p}\right).} \tag{5.3}
\]

The first term charges every completion at the primitive-row period. The
nonnegative correction restores the cost of the symmetric rows. No row is
incorrectly declared primitive.

At small core size a<=60, the program computes all the proper-period quantities
in (5.3) exactly. At larger a it uses the following faster valid correction.

### 5.1 An explicit bound for all symmetric rows

The preceding `EXACT_PERIOD_CENSUS.md`, Section 6.3, proves that the total number
b_a of size-a roots with nonprimitive top row satisfies

\[
 b_a\le43(25/9)^a.
\]

Its proof is finite: evaluate the nonnegative generating function for repeated
rows at x=9/25, bound the Narayana peak polynomial by its binomial product, and
sum a geometric series. It does not assume profile concentration. Therefore

\[
 B_a:=\left\lfloor43\frac{25^a}{9^a}\right\rfloor
\]

is an integer upper bound. In the current (a,b) class there are at most
min(K(a,b),B_a) symmetric roots. Their original height is at most s+b+1.
Since P_d>=P, the correction in (5.3) is bounded by

\[
 w(2s+2b+1)\min(K(a,b),B_a)
       \left(\frac1P-\frac1{P_p}\right). \tag{5.4}
\]

Use Hhat in the baseline term. Both coefficients are nonnegative, so these
separate upper bounds may be substituted without a covariance or independence
assumption. Finally take the minimum with (3.3), using Hhat, and with the old
height-cap bound. Each term is rounded upwards before integer comparison.

This improves a prefix bound without creating a separate child for every
possible next size. Updating such a bound never invalidates the frontier.
For exact heights and unrounded charges, (5.2) is also no larger than (3.3).

## 6. Sparse expansion with an explicit reserve

Sometimes a prefix still needs to be split. It is wasteful to instantiate all
of its next-size values when almost all mass is near the mode. There is a safe
way to leave the tails unexpanded.

The exact completion mass at a next-size value c, before splitting row periods,
is

\[
 w\binom{a+c}{2b}K(b,c). \tag{6.1}
\]

For ANY chosen set of next-size values, expand all row periods at those values.
Let M_rem be the parent completion count minus the exact masses of the created
children. By (2.5), M_rem is the exact number of unexpanded completions.
Their contribution is bounded by the explicit reserve

\[
 \boxed{\frac{M_{\rm rem}(2s+2b+1)}P.} \tag{6.2}
\]

The reserve is retained in the global certificate even though it is never
expanded further. In particular, this is not truncation of a small probability
without paying for it.

For efficiency the program visits c-values near a mode first. The exact ratio
of their weights is

\[
 \frac{a+c+1}{a+c+1-2b}
 \frac{(b-c)(b-c-1)}{(c+1)(c+2)}. \tag{6.3}
\]

It is decreasing, so a mode can be located by integer comparisons. Moving right
or left updates the two binomial factors by exact ratios. The correctness of
(6.2) does not depend on this ordering. A transcript stores how many c-values
were expanded at each split; the independent replay reconstructs their exact
set and mass.

The implemented stopping rule for a split is that its reserve charge is no more
than max(1,floor(old_integer_charge/65536)). This numerical rule only affects
efficiency. The final inequality always includes the actual reserve charge.

## 7. The integer certificate and the uniform theorem

Maintain a frontier of exact prefix families and frozen reserves. Ordinary
families carry their valid integer upper charges from Sections 3--5; reserves
carry the upward-rounded charge in (6.2). Let their sum be U_r. Then

\[
 \boxed{N_r-W_r\le(2r+1)U_r.} \tag{7.1}
\]

The invariant behind the computation is that all frontier and reserve masses
sum to Cat_r. A moment update changes no mass. A split preserves mass exactly,
including its reserve. Ceilings only increase the bound. Thus

\[
 100000U_r<\operatorname{Cat}_r \tag{7.2}
\]

is a valid ten-parts-per-million certificate.

The delivered transcript collection verifies (7.2) for EVERY integer

\[
 68\le r\le3423,
\]

namely 3356 cases. These are integer inequalities, not a sampled or interpolated
set of dimensions. The machine-readable file records each Catalan denominator,
upper numerator, positive comparison margin, upgrade and split transcript, and
explicit reserve accounting. The executed summary states the separate replay
scope. The huge universal words themselves were not materialized.

### 7.1 The decreasing analytic tail

Retain the explicit envelope from `EXACT_PERIOD_CENSUS.md`, Section 6:

\[
 J_r=\frac1{r(r+2)}+
       \frac{40}{3r(r+2)(r+3)}+
       \frac{43}{72\operatorname{Cat}_r},
\]

\[
 \frac{N_r-W_r}{W_r}\le E_r:=
 2\sqrt{\frac{2J_r}{2r+1}}+
 86(r+1)\sqrt r(25/36)^r. \tag{7.3}
\]

All positive summands of J_r decrease. For r>=4 the square of the ratio of the
second term at r+1 to its value at r is at most 125/144<1, because

\[
 9r(r+1)-5(r+2)^2=(r-4)(4r+5)\ge0.
\]

So E_r decreases for all r>=4. The present audit recomputes square roots from
above by integer square roots and obtains the rational certificate

\[
 \boxed{E_{3424}<
  \frac{9998021412265816178}{10^{24}}<\frac1{100000}.} \tag{7.4}
\]

Thus the transcript band covers r=68,...,3423 and the analytic envelope covers
EVERY r>=3424. There is no use of monotonicity of the actual construction length.
Together they establish the odd-dimensional bound for all r>=68.

For the following even dimension, the standard trimmed lift sends an old word
Q_1,...,Q_N to

\[
 Q_1,\ldots,Q_N,\{z\},Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}.
\]

It has 2N letters and is universal: old targets keep their witnesses; a marked
target with an old witness ending at N uses that suffix followed by {z}; all
other marked targets use the translated copy. Since W(2r+2)=2W_r, its relative
excess is unchanged. This proves T1 for every k>=2*68+1=137.

## 8. The predecessor obstruction is construction-specific

The predecessor transcript at r=67 retains only some completed terminal
families. Each such family of w roots has exact height h and exact period v,
and contributes exactly (2r+1)w(2h-1)/v to the construction collar. All omitted
families have nonnegative contributions. Summing the terminal families therefore
gives a rigorously certified LOWER bound C_low on that collar.

The delivered transcript and independent replay verify

\[
 100000 C_{\rm low}>(2*67+1)\operatorname{Cat}_{67}=W(135). \tag{8.1}
\]

Thus the unchanged construction fails the target at 135; its prescribed doubled
word fails at 136. Combined with T1, 137 is the smallest uniform starting
dimension for THIS constructor and THIS lift. It is not claimed to be the
smallest such dimension for nu(k), since another word may be shorter.

## 9. Checks, replay and limitations

`verify_moment_prefix.py` contains the complete arithmetic generator with no
import of an earlier verifier. `audit_moment_prefix.py` supplies independent
Dyck enumeration and physical cycle traversal, and a transcript consumer that
uses a dictionary rather than the search priority queue. It reconstructs all
masses, upgrades, sparse splits and reserves and checks the final inequality.

The structural audit independently checks the new conditional height totals
against all 23713 nonempty Dyck roots through semilength 10; checks conditional
row-period height totals; checks all scalar periods against 125475 middle
states through dimension 19; and verifies the reflection tail bounds and
primitive-baseline correction identities with integer or rational arithmetic.
The actual execution summary records the complete finite-band and replay counts.

Neither these computations nor the preceding package formally verify the
inherited all-dimension corridor theorem. No dimension-17 word is read or
modified. Exact equality nu(k)=B(k) and the previously discussed asymptotic
power improvements are not established by this continuation.

### Reproduction

Run the structural audit:

```text
python audit_moment_prefix.py --structural --out structural_checks.json
```

Replay the supplied full certificate collection without the search heuristic:

```text
python audit_moment_prefix.py --replay moment_certificates.jsonl.gz --complete-band --out replay.json
```

Regenerate a band (the output goes in `batches/`):

```text
python verify_moment_prefix.py --start 68 --end 3423 --target 100000 --out regenerated
```

No running-time claim polynomial in r or in the requested accuracy is made.

### Sources and contribution boundary

- `PREFIX_PERIOD_BOUND.md`, Sections 2--5: exact forward denominator period,
  prefix masses, old height-cap charges and integer certificates.
- `EXACT_PERIOD_CENSUS.md`, Sections 2--7: exact row-period fibres, Narayana law,
  reflection identities, total nonprimitive-row count and decreasing envelope.
- `HEIGHT_ADAPTIVE.md`, Sections 2--5: full-cube construction and strict-height
  corridor dependency.
- `FULL_PROOF_TEXT (1).txt`, Document 19 Sections 14 and 21 and Document 32
  Sections 1--2: inherited finite particle, matching and fibre premises.
- The authoritative handoff, Section 2: B(k)<=nu(k).

The new deductions here are the height-total recurrence, its unfinished-prefix
charge, the finite reflection-subfamily bound, the integrated row-period
correction and the complete sparse-reserve certificates. General PBBS period
formulas predate this work (Yoshihara--Yura--Tokihiro, arXiv:nlin/0208042);
that outside theorem is not used in the new argument.
