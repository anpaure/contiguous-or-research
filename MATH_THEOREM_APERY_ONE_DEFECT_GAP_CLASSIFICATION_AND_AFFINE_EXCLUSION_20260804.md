# Cyclic Apéry clocks with one exceptional gap

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical classification and a conditional
exclusion inside the all-grid no-descent branch.  It does not prove the
remaining long-wrap family positive and does not prove universal Bellman
positivity.

Put

\[
 A={\sqrt\pi\over2}.
\]

Let

\[
 0=s_0<s_1<\cdots<s_{h-1}<P,
 \qquad h\ge3,
\tag{0.1}
\]

be an honest cyclic Apéry table.  The restriction `h>=3` makes “all but
one gap have a common value” a genuine one-defect hypothesis; with two
gaps either one can be declared the exceptional one.  The two-gap
first-carry case belongs to the already proved three-slot theorem.

The shifts satisfy the carry-aware
superadditivity inequalities

\[
 s_{r+t}\ge s_r+s_t\quad(r+t<h),
\qquad
 P+s_{r+t-h}\ge s_r+s_t\quad(r+t\ge h).
\tag{0.2}
\]

Write its cyclic gaps as

\[
 \gamma_1=s_1,
 \quad \gamma_j=s_j-s_{j-1}\ (2\le j<h),
 \quad \gamma_h=P-s_{h-1}.
\tag{0.3}
\]

The associated exact periodic clock is

\[
 W_{qh+r}=qP+s_r
 \qquad(q\ge0,\ 0\le r<h).
\tag{0.4}
\]

## 1. Classification theorem

### Theorem 1.1 (one-defect cyclic-gap classification)

Suppose all but at most one of the gaps in (0.3) equal one number
`a>0`.  Then exactly one of the following occurs.

1. **Uniform:** every gap equals `a`.
2. **Short first gap:**

   \[
   (\gamma_1,\ldots,\gamma_h)=(t,a,\ldots,a),
   \qquad0<t<a.
   \tag{1.1}
   \]

3. **Long wrap gap:**

   \[
   (\gamma_1,\ldots,\gamma_h)=(a,\ldots,a,t),
   \qquad t>a.
   \tag{1.2}
   \]

In particular, a genuine lone exceptional gap cannot occur at an internal
position `2<=j<=h-1`.

#### Proof

First, every cyclic gap is at least the first gap.  For `2<=j<h`, apply
the first inequality in (0.2) to `(j-1)+1`:

\[
 s_j\ge s_{j-1}+s_1,
\]

so `gamma_j>=gamma_1`.  Applying the carry inequality to
`(h-1)+1=h` gives

\[
 P\ge s_{h-1}+s_1,
\]

so `gamma_h>=gamma_1` as well.

Consequently, if the exceptional gap is first then it is no larger than
the common gap; equality is the uniform case, and strict inequality gives
(1.1).  If the exceptional gap is the wrap gap, it is no smaller than the
common first gap; equality is uniform, and strict inequality gives (1.2).

It remains to exclude an internal exceptional position `j`.  Write

\[
 \gamma_j=a+\delta,
 \qquad 2\le j\le h-1.
\tag{1.3}
\]

The preceding minimum-gap argument gives `delta>=0`.  Also

\[
 P=ha+\delta,
\quad
 s_r=
 \begin{cases}
  ra,&r<j,\\
  ra+\delta,&r\ge j.
 \end{cases}
\tag{1.4}
\]

If `j<=h/2`, use (0.2) with the two indices `j` and `h-j`.  Both are at
least `j`, so

\[
 ha+2\delta=s_j+s_{h-j}\le P=ha+\delta.
\]

Hence `delta<=0`.

If `j>h/2`, use (0.2) with `j+j`.  Now `2j-h<j`, and therefore

\[
 2ja+2\delta=2s_j
 \le P+s_{2j-h}
 =(ha+\delta)+(2j-h)a
 =2ja+\delta.
\]

Again `delta<=0`.  Thus `delta=0` in either case, contrary to a genuine
exception.  This proves the classification. \(\square\)

## 2. The short-first case is exactly affine setup cost

Assume (1.1), and put

\[
 \alpha=a,
 \qquad \beta=a-t\in(0,a).
\tag{2.1}
\]

Then

\[
 s_r=t+(r-1)a=ra-\beta\quad(1\le r<h),
 \qquad
 P=t+(h-1)a=ha-\beta.
\tag{2.2}
\]

Consequently (0.4) becomes

\[
 \boxed{
 W_m=\alpha m-\beta\left\lceil{m\over h}\right\rceil.}
\tag{2.3}
\]

This is precisely the affine setup-cost Bellman clock.

### Corollary 2.1 (exact first-carry affine exclusion)

Suppose in addition that the first threshold crossing is the first carry
after one period and is exact:

\[
 P<A,
 \qquad P+t=A.
\tag{2.4}
\]

Set `n=h+1`.  Then

\[
 A=(h+1)a-2\beta= n\alpha-2\beta,
\tag{2.5}
\]

and

\[
 0<\beta<{A\over n-2}.
\tag{2.6}
\]

Hence the clock is a member of the complete all-grid affine setup-cost
family and has strictly positive Gaussian Bellman functional.

#### Proof

Equation (2.5) is (2.2) and (2.4).  Since `beta<a`,

\[
 (n-2)\beta=(h-1)\beta
 <(h+1)a-2\beta=A,
\]

which is (2.6).  The audited all-grid affine theorem applies. \(\square\)

The endpoint `beta=0` is the uniform arithmetic clock and is strictly
positive by reciprocal-ceiling positivity.

## 3. The sole one-defect survivor

On the long-wrap face (1.2), put `delta=t-a>0`.  Then

\[
 s_r=ra\quad(0\le r<h),
 \qquad P=ha+\delta,
\tag{3.1}
\]

and the exact clock is

\[
 \boxed{
 W_m=am+\delta\left\lfloor{m\over h}\right\rfloor.}
\tag{3.2}
\]

Thus the only genuine one-defect cyclic geometry not covered by the
affine closure is a **period-dilated arithmetic clock**: every completed
period receives a nonnegative bonus, equivalently the wrap gap is longer
than every internal gap.

There is nevertheless a uniform positive subrange at the exact first
carry.  Suppose

\[
 P<A,
 \qquad P+a=A.
\tag{3.3}
\]

Adjoin the inert endpoint value `A` at capacity `h+1`.  The resulting
first-crossing table is

\[
 (0,a,2a,\ldots,(h-1)a,A-a,A).
\tag{3.4}
\]

For the threshold-period train put

\[
 F(w)=\sum_{q\ge0}K(qA+w),
 \qquad C=F(0).
\tag{3.5}
\]

The literal endpoint-period comparison gives

\[
 \boxed{
 \Phi(W)\ge
 C+\sum_{i=1}^{h-1}F(ia)+F(A-a).}
\tag{3.6}
\]

Indeed, at capacity `(h+1)q+i` use `q` endpoint generators together with
the displayed size-`i` generator.  For `q>=1` the comparison lies in the
increasing Gaussian tail; at `q=0` it is equality.

The exact Jacobi reflection bound and the authenticated compact train
bounds are

\[
 F(a)+F(A-a)>-{1\over20000},
 \qquad C>{43\over1000},
 \qquad F(w)>0\quad(0\le w\le A/2).
\tag{3.7}
\]

Consequently, if

\[
                         (h-1)a\le {A\over2},
\tag{3.8}
\]

then all terms `F(ia)` with `2<=i<=h-1` are positive, while the first and
last shifts in (3.6) form the reflected pair in (3.7).  Therefore

\[
 \boxed{
 \Phi(W)> {43\over1000}-{1\over20000}>0.}
\tag{3.9}
\]

Since the long-wrap condition and (3.3) give

\[
 a< {A\over h+1},
\tag{3.10}
\]

the inequality being strict because
`delta=A-(h+1)a>0`,

the only long-wrap exact-first-carry range not closed by (3.9) is

\[
 \boxed{
 h\ge4,
 \qquad {A\over2(h-1)}<a< {A\over h+1}.}
\tag{3.11}

Thus every one-defect exact-first-carry clock in this theorem is positive
for `h=3`; the omitted `h=2` case is positive by the complete three-slot
Bellman theorem.
For arbitrary `h`, the sole unresolved part is the narrow near-uniform
long-wrap interval (3.11).  No sign is asserted there.  In particular,
deleting the omitted arithmetic points can delete compact positive kernel
terms, so positivity in (3.11) does not follow merely by comparing with the
full arithmetic clock.

## 4. Consequence for the all-grid trichotomy

Consider branch C of the audited minimal-counterexample Apéry trichotomy.
Write `V` for the original clock, `W` for its formal cyclic Apéry clock,
and

\[
 \Phi(V)=\Phi(W)+\mathcal H(V,W)
\tag{4.1}
\]

for the exact finite shoulder decomposition.  Suppose that `W` first
crosses exactly at `N=g+1`, with `W_N=A`.

If `Phi(W)<=0` and its cyclic gap word has at most one exceptional gap,
then `W` must be of the long-wrap form (3.2), with parameters in the
narrow range (3.11).  Indeed:

* the uniform face is an arithmetic ceiling clock and is positive;
* the short-first face is positive by Corollary 2.1; and
* Theorem 1.1 excludes an internal lone defect; and
* (3.9) closes the broad long-wrap range and every `g<=3` case.

Consequently every original nonpositive exact-first-carry branch-C clock
falls into exactly one of the following three alternatives:

1. **Finite shoulder:** `Phi(W)>0` and

   \[
   \mathcal H(V,W)\le-\Phi(W)<0.
   \tag{4.2}
   \]

2. **Pure periodic one-defect:** `Phi(W)<=0` and the gap word is a
   near-uniform long wrap as in (3.11).

3. **Pure periodic multidefect:** `Phi(W)<=0` and no number is shared by
   all but at most one cyclic gap.

In particular, the formal-clock nonpositive branch has the sharp
structural narrowing

\[
 \boxed{
 \text{near-uniform long wrap as in (3.11), or at least two
 noncommon cyclic gaps}.}
\tag{4.3}
\]

This is a strict structural narrowing of the no-descent carry branch.  It
does not address threshold overshoot `W_N>A`, a later first crossing
`N>g+1`, elimination of the finite-shoulder alternative (4.2), or the
endpoint-critical branch.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| all-grid affine positivity | `MATH_THEOREM_REFLECTED_COMPACT_SLOPE_FULL_HALF_INTERVAL_AND_ALL_GRID_AFFINE_CLOSURE_20260804.md` | `2c37dfcd8d05231cd3cd60e4babe3cf1c22b54e869f716665c08511d3fcf4c2f` |
| affine theorem audit | `MATH_AUDIT_REFLECTED_COMPACT_SLOPE_FULL_HALF_INTERVAL_AND_ALL_GRID_AFFINE_CLOSURE_INDEPENDENT_20260804.md` | `1eab4ff6511032248ce92c1e37b6caafc8a44cfb67c98b3c7b6b674aa28b79a2` |
| strict reciprocal-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
| reciprocal-ceiling audit | `MATH_AUDIT_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `d5be0518e8a48540f6877066e8292029b23b7803079d06d53071b844bae5c681` |
| threshold train reflection and compact positivity | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_THRESHOLD_SURFACE_CLOSURE_20260804.md` | `7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b` |
| threshold train audit | `MATH_AUDIT_FOUR_SLOT_THREE_EFFICIENT_THRESHOLD_SURFACE_CLOSURE_INDEPENDENT_20260804.md` | `090494f7180f211752635415294b4fd5f341cded2362de9c46aaf19eb6aea1c4` |
| sharp threshold ceiling margin | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| threshold ceiling-margin audit | `MATH_AUDIT_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_INDEPENDENT_20260804.md` | `6d07121018046f26f4ab5377e37dd692efffa8389b9d939668e2f1a73ae14425` |
| complete three-slot positivity | `MATH_THEOREM_THREE_SLOT_BELLMAN_NORMAL_FORM_AND_SCALAR_GATE_20260804.md` | `460ff642edef6ff0164247c66f09e0d1896b9db5c541a9e0034e076b8f423219` |
| three-slot audit | `MATH_AUDIT_THREE_SLOT_BELLMAN_NORMAL_FORM_AND_SCALAR_GATE_20260804.md` | `fb1b5651c35f44b8d816c25a340a5b28ae3fa888b0aac1a679b10bf23519a633` |
| all-grid Apéry trichotomy | `MATH_THEOREM_ALL_GRID_MINIMAL_COUNTEREXAMPLE_APERY_DESCENT_TRICHOTOMY_20260804.md` | `8ed0ae35fe1a3bbd52824bca67240155868ed1e3a268b1f582aba944e081b4b2` |
| trichotomy audit | `MATH_AUDIT_ALL_GRID_MINIMAL_COUNTEREXAMPLE_APERY_DESCENT_TRICHOTOMY_INDEPENDENT_20260804.md` | `62234f7a72b151d78be1320099463048988417114c677f03f0178849ba00b7b9` |
