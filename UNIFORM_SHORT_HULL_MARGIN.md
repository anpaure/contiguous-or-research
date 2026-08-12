# Uniform margin for every nonabsorbed short hull

## 1. Statement

Fix a threshold

\[
                     1<c<{4\over3}.
\]

For normalized consecutive dangerous-plateau data let

\[
 p,s\ge c,\qquad z\ge0,\qquad p+s+z\le4,
\]

and use the self-closed nonabsorbed cost

\[
 C_c(p,s,z)=p\min(c,z)+z\min(p,s).
\]

Define

\[
 D_c(p,s,z)={4\over3}(p+z)-C_c(p,s,z),
 \qquad
 K(c)=\left({4\over3}-c\right)(2-c).
\]

Then

\[
 \boxed{D_c(p,s,z)\ge K(c)>0.}                     \tag{1.1}
\]

Equality is unique:

\[
             p=s={4-c\over2},\qquad z=c.           \tag{1.2}
\]

Thus self-closure of the complete dangerous list removes not only the old
neutral triple, but every zero-margin nonabsorbed short-hull profile.

## 2. Proof of the pointwise inequality

Put `m=min(p,s)`.

### Case A: `z<=c`

Here

\[
 D_c={4\over3}(p+z)-z(p+m).
\]

For fixed `p,s` this is affine in `z`, with slope
`4/3-p-m<0`.  Hence the minimum occurs at

\[
                    z=\min(c,4-p-s).                \tag{2.1}
\]

If `z=c` and `p<=s`, then

\[
 D_c={4c\over3}+p\left({4\over3}-2c\right).
\]

The coefficient of `p` is negative and feasibility gives
`p<=(4-c)/2`; the minimum is therefore attained at
`p=s=(4-c)/2`.  If `s<=p`, first replace `p` by `s`, which can only decrease
the expression because `4/3-c>0`, and obtain the same minimum.

If instead `z=4-p-s`, fix `z`.  When `s<=p`,

\[
 D_c={4\over3}(p+z)-z(4-z),
\]

and it is minimized at `p=s=(4-z)/2`.  When `p<=s`,

\[
 D_c={4z\over3}+p\left({4\over3}-2z\right).
\]

For `z>=2/3` it is again minimized at the balanced endpoint.  For
`z<2/3` it is minimized at `p=c`, and the value is at least `8/9`, which
is strictly larger than `K(c)`.  At the balanced endpoint the value is

\[
 F(z)=z^2-{10\over3}z+{8\over3}.
\]

On the relevant interval `z<=c<4/3`, `F` is decreasing, so

\[
 F(z)\ge F(c)=\left({4\over3}-c\right)(2-c)=K(c).
\]

### Case B: `z>=c`

Now

\[
 D_c=p\left({4\over3}-c\right)
       +z\left({4\over3}-m\right).                 \tag{2.2}
\]

If `m<=4/3`, minimize in `z` at `z=c` and invoke Case A.  If
`m>=4/3`, minimize at `z=4-p-s`.  In the subcase `p<=s`, decrease `s` to
`p`; in the subcase `s<=p`, decrease `p` to `s`.  Both reduce to

\[
 f(t)=t\left({4\over3}-c\right)
      +(4-2t)\left({4\over3}-t\right),
 \quad {4\over3}\le t\le{4-c\over2}.
\]

Here

\[
 f'(t)=4t-\left({16\over3}+c\right)<0
\]

throughout the interval.  Its minimum is at `t=(4-c)/2`, where `z=c`
and the value is `K(c)`.  Tracing equality through the cases proves the
uniqueness assertion (1.2).

## 3. Global consequence

At this threshold split the short-hull seam measure into nonabsorbed and
absorbed parts `rho_N,rho_A`, and let `b` be normalized bad-hull and boundary
**word mass**.  Put

\[
 m_N=\|\rho_N\|,\qquad E=\|\rho_A\|+b.
\]

The two-sided assignment inequality, the absorbed excess bound
`Delta_A<=2/3`, and (1.1) give

\[
 {Q\over a^3}\le4-K(c)m_N+{2\over3}E+o(1).
\]

In the subquadratic-defect branch every admissible assignment has
`Q/a^3>=4-o(1)`, hence

\[
                         K(c)m_N\le{2\over3}E+o(1). \tag{3.1}
\]

The word-mass identity is

\[
 3\le (4-c)(m_N+\|\rho_A\|)+b+o(1)
   \le(4-c)(m_N+E)+o(1),                            \tag{3.2}
\]

because every short record has `p+z<=4-c`.  Combining (3.1)--(3.2) yields

\[
 \boxed{
 E\ge {3K(c)\over(4-c)(K(c)+2/3)}-o(1).}            \tag{3.3}
\]

At `c=13/12`, this is

\[
 K={11\over48},\qquad E\ge{396\over1505}-o(1)
                         =0.26312\ldots-o(1).
\]

As `c` decreases to one, the right side tends to `1/3`.

## 4. Scope

The theorem seals the entire neutral/nonabsorbed branch.  It does not by
itself exclude a process carrying the mandatory positive mass in absorbed
seams or bad long hulls.  The remaining task is to charge that mass against
direction-labelled positive-line energy and the bad-gap budget at the same
threshold.
