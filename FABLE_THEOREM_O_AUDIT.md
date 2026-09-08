# Independent audit of Fable Section 10.3 (Theorem O) and Section 10.4

## 1. Verdict

The **main statement of Theorem O is correct**:
`FIRST_DANGEROUS_GLOBAL_SERVICE` extends from fixed `1<c<2` to every
fixed `0<c<2`.  More precisely, with constants allowed to depend on the
fixed threshold `c`,

\[
 Q\le caM_a+2a\sum_j\delta_j
   +\sum_{j\ge2}\delta_j\min\{g_{j-1},L-\lambda_j\}
   +O_c(a^2).
\]

The same forward assignment has span and endpoint congestion at most
`4a+3`, and omits `O_c(a)` indices.  The normalized mass law

\[
                  2e(c)+H(c)\ge4-3c-o(1)
\]

therefore holds at every fixed `0<c<4/3` under the inherited
`D=o(a^2)` hypothesis.

Section 10.4, however, contains a decisive notation/concept error.  It
identifies normalized **weighted supply** with the unweighted number of
plateaux above the threshold.  They are not the same:

\[
 \operatorname{Sup}(c)
   =\int_{(c,2]}(4-x)\,d\mu(x),
 \qquad
 F(c)=\mu((c,2]).
\]

Theorem N proves a lower bound on `Sup(c)`, not the same lower bound on
`F(c)`.  Consequently the claims that supply forces `2a` plateaux at
`c -> 0`, that the scalar survivor is forced to `2 delta_(3/2)`, and that
the remaining geometry is necessarily near edge-saturated are not proved
and are false for the displayed scalar system.

The explicit profile

\[
                         \mu=2\delta_{4/3},\qquad H=0
\]

passes every correctly stated scalar inequality.  In fact the continuum
`2 delta_x`, `4/3 <= x <= 3/2`, does so.  Thus the proposed
“near-saturated dense-chain corner” is only one possible corner, not a
forced reduction.

## 2. Line-by-line audit of Theorem O

Throughout this section `c` is fixed and positive.  This qualification is
essential: the estimates are not uniform as `c -> 0` because the number of
dangerous plateaux is only `O_c(a)`.

### 2.1 Dangerous-free window lemma

This step is independent of `c>1`.  The peak-mesh theorem supplies a complete
internal peak plateau in the window.  If its cost is at most `ca`, it is a
cheap run.  If its cost exceeds `ca` but it is nondirected, a cross coordinate
has an interior strict extremum, yielding a cost-zero singleton peak.  Hence
the lemma works for every `c>0`.

For a fixed positive `c`, eventually `ca>1`; no integer-rounding issue changes
the asymptotic estimate.

### 2.2 Ordering and first-dangerous localization

Distinct maximal constant-coordinate plateaux share no ordering edge and at
most one endpoint.  Thus, in word order,

\[
                         v_{j-1}\le u_j.
\]

If a forward start assigned to `P_j` lay before `u_(j-1)`, containment of
`P_j` would also imply containment of the earlier `P_(j-1)`, contradicting
the first-dangerous rule.  Therefore

\[
 n_j\le\min\{L-\lambda_j,
              \lambda_{j-1}+1+g_{j-1}\}.
\]

No threshold inequality occurs here.  The proof remains valid for all
`c>0` under the already audited convention that shared endpoints remain in
the plateau vertex union.

### 2.3 Cost ledger and predecessor term

Writing `delta_j=lambda_j-ca>=0`, the proof reaches

\[
 \sum_j\delta_jn_j
 \le \sum_j\delta_j\lambda_{j-1}
     +\sum_{j\ge2}\delta_j\min\{g_{j-1},L-\lambda_j\}
     +O(a^2),
\]

where the first sum is made cyclic by adding a nonnegative closing term.
For every plateau, independently of `c`,

\[
                         \lambda_{j-1}\le2a.
\]

Hence directly

\[
 \sum_j\delta_j\lambda_{j-1}
          \le2a\sum_j\delta_j.                    \tag{2.1}
\]

This proves exactly the required coefficient.  Fable's observation is
correct.  In fact the original secant inequality also extends to the whole
range `0<c<2`: after writing `x=ca+u`, `y=ca+v` and
`0<=u,v<=(2-c)a`, it reduces to

\[
                         2uv\le(2-c)a(u+v),
\]

which is valid for all such `u,v`.  Thus there are two independent ways to
remove the old `c>1` restriction.

The first-plateau contribution is `O(a^2)`, and
`sum delta_j <= sum lambda_j <= M_a-1=O(a^2)`, uniformly in fixed `c`.

### 2.4 Number of plateaux and omissions

Dangerous plateau edge sets are disjoint and each has more than `ca` edges,
so

\[
 mca<\sum_j\lambda_j\le M_a-1,
 \qquad m=O_c(a).
\]

Therefore optional omission of their shared endpoints costs `O_c(a)` starts,
and its fan-capped contribution is `O_c(a^2)`.  This is the sole material
place where positivity and fixedness of `c` enter.  The notebook should say
`O_c(a)` rather than suggest a uniform constant.

The theorem does **not** license substituting a threshold `c=c(a)->0`
without a separate uniform-error argument.  Sequential consequences—first
fix `c`, let `a->infinity`, and only then let `c->0`—are legitimate.

### 2.5 Seam bounds

Both inherited seam estimates remain valid because

\[
 0\le\delta_j\le(2-c)a,
 \qquad L-\lambda_j=(4-c)a+2-\delta_j.
\]

Thus

\[
 H(c)\le(4-c+o(1))e(c),
 \qquad
 H(c)\le(2-c)(3-\sigma)+o(1).
\]

The gap-count error is `o(1)` after normalization precisely because
`m=O_c(a)`.

### 2.6 Span and congestion

Every chosen run lies in `[i+1,i+L]`; all assignments point forward.  Hence
the one-sided span and `alpha` congestion are at most `L+1=4a+3`, while the
opposite congestion is zero.  This is independent of `c`.

These checks prove Theorem O for every fixed `0<c<2`.

## 3. Audit of the consequences stated in Section 10.3

### 3.1 Mass law

**Correct.**  Combining the service upper bound with Theorem I under
`D=o(a^2)` gives, for each fixed `0<c<4/3`,

\[
                         2e(c)+H(c)\ge4-3c-o(1).
\]

### 3.2 Supply law

**Correct only with the old Section 9 meaning of `s(c)`: normalized weighted
supply.**  To avoid the collision with plateau count, write

\[
 S(c):={\operatorname{supply}(ca)\over a^2}.
\]

Then Theorem N gives

\[
                         S(c)\ge{4-3c\over2-c}-o(1).
\]

It does not give this inequality for the count tail `F(c)/a`.

### 3.3 The `c -> 0` plateau count

The statement that supply forces at least `(2-o(1))a` plateaux is **false**.
Every plateau above threshold `c` contributes at most `(4-c)a+O(1)` to
supply.  The valid consequence is

\[
 {F(c)\over a}
 \ge {4-3c\over(2-c)(4-c)}-o(1).                  \tag{3.1}
\]

At `c -> 0` this gives only

\[
                         F(0+)/a\ge1/2-o(1),
\]

not two.  At `c=1` it gives the already audited `1/3`.

If additionally `H(c)->0` as `c->0`, the **mass** law does imply
`sigma>=2`; that separate low-seam conclusion is valid.  It does not imply
that the mass is split among `2a` plateaux.

### 3.4 The old unit atom

For `mu=delta_(3/2)` and `H=0`, at `c=1/2`,

\[
 e(c)=1,
 \qquad 2e(c)=2<5/2=4-3c.
\]

Thus the extended **mass law** kills this counterprofile.

The supply law does not kill it.  Its actual normalized supply is

\[
 S(c)=4-3/2=5/2
\]

for every `c<3/2`, which easily exceeds the required `5/3` at `c=1/2`.
The notebook's contrary supply claim uses plateau count in place of supply.

### 3.5 Ring and random orders

The `D=Omega(a^2)` conclusions for contiguous-ring and uniformly random
orders remain valid, but they do not depend on Theorem O.  As Section 10.2
observes, both already follow at the fixed threshold `c=6/5`, inside the
previously certified range `1<c<2`.  The Section 10.4 supply/count error does
not affect those two conclusions.

## 4. Correct profile formulation for Section 10.4

For the normalized counting measure

\[
                 \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a},
\]

the relevant quantities, at continuity points of the limiting tails, are

\[
\begin{aligned}
 F(c)/a &\longrightarrow \mu((c,2]),\\
 e(c)   &=\int(x-c)_+\,d\mu(x),\\
 \sigma &=\int x\,d\mu(x),\\
 S(c)   &=\int_{(c,2]}(4-x)\,d\mu(x).
\end{aligned}                                      \tag{4.1}
\]

The strict tail `(c,2]` matches `lambda>ca`; atom-boundary conventions can
be handled by one-sided limits.

The scalar ledger that is actually proved is therefore

\[
\begin{array}{ll}
\text{(i)}&\sigma\le3,\\
\text{(ii)}&\mu([x,2])\le6(2-x)\quad(x>1),\\
\text{(iii)}&2e(c)+H(c)\ge4-3c,\\
\text{(iv)}&S(c)\ge(4-3c)/(2-c),\\
\text{(v)}&0\le H(c)\le
 \min\{(4-c)e(c),(2-c)(3-\sigma)\}.
\end{array}                                        \tag{4.2}
\]

The count consequence (3.1) may be appended, but it is strictly weaker than
the false count inequality written in Section 10.4.

## 5. Explicit surviving profiles

### 5.1 Requested audit: `mu=2 delta_(4/3)`, `H=0`

For every `0<c<4/3`,

\[
 \sigma={8\over3},
 \qquad e(c)={8\over3}-2c,
 \qquad S(c)={16\over3}.
\]

It satisfies the mass law because

\[
 2e(c)-(4-3c)={4\over3}-c\ge0.
\]

It satisfies the weighted supply law since `16/3` is larger than its
right-hand side (whose maximum is two).  The line-capacity inequality holds:
below the atom its tail is two and
`2<=6(2-4/3)=4`; above the atom its tail is zero.  Finally `sigma<3` and
`H=0` satisfies both seam upper bounds.

Therefore this profile passes the complete corrected scalar system while
retaining a positive edge-budget gap `3-sigma=1/3`.  It directly refutes the
claim that the surviving profile is forced to be edge-saturated.

### 5.2 A continuum, not a unique corner

More generally,

\[
                         \mu=2\delta_x,\qquad H=0
\]

passes (4.2) for every

\[
                         {4\over3}\le x\le{3\over2}.
\]

Indeed, `sigma=2x<=3`; the mass-law difference is
`4x-4-c`, minimized as `c->4/3` and nonnegative exactly when
`x>=4/3`; line capacity is valid throughout this interval; and weighted
supply equals `2(4-x)>=5`.

The endpoint `x=3/2` is the edge-saturated member, but nothing in the scalar
system forces that endpoint.  Even the erroneous unweighted count inequality
would be satisfied by this whole continuum, since its tail is two throughout
`0<c<4/3`.

## 6. Consequence for the proposed next lemma

The conditional statement

> if `sigma->3`, then the second seam bound forces `H->0`

is correct.  What fails is the preceding claim that the scalar laws force
`sigma->3`.  Hence a level ledger dealing only with asymptotically saturated,
gap-free chains would not close the scalar obstruction: it would leave, for
example, `2 delta_(4/3)` untouched.

The mathematical program must either

1. prove an additional inequality forcing `sigma` toward three or excluding
   the unsaturated atom continuum;
2. obtain a geometric ledger that also rules out dense chains with
   `sigma` in `[8/3,3)`; or
3. exploit information not represented by `(mu,e,S,H,sigma)`.

## 7. Final ledger

### Certified

* Theorem O's first-dangerous service estimate for every fixed `0<c<2`.
* Its span, congestion, and `O_c(a)` omission bounds.
* The mass law for every fixed `0<c<4/3` under `D=o(a^2)`.
* The weighted supply law from Theorem N.
* The correct plateau-count consequence (3.1).
* The unit atom `delta_(3/2)` is excluded by the mass law.

### Retracted or unsupported

* `s(c)=mu([c,2]) >= (4-3c)/(2-c)` as a plateau-count law.
* At least `(2-o(1))a` plateaux from supply at `c->0`.
* Exclusion of `delta_(3/2)` by supply rather than by mass.
* Uniqueness of `2 delta_(3/2)` as the surviving scalar corner.
* The claim that every scalar survivor is near edge-saturated and therefore
  reduced to the proposed general-pattern dense-chain ledger.
