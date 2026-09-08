# Scalar slack: parity unification, dyadic granularity, and equidistribution

## Status and scope

This note studies only the scalar slack

\[
 \sigma(k)=dW+\binom{d+1}{2}-\Lambda,
 \qquad
 W=\binom{k}{\lceil k/2\rceil},
 \qquad
 \Lambda=\sum_{s=1}^{\lceil k/2\rceil-1}\binom{k}{s},
\]

where \(d\) is the least nonnegative integer for which the displayed
slack is nonnegative.  It does not construct a word or round a fractional
factor.

The main conclusions are deliberately two-sided.

1. There is an exact parity-unified formula and an exact dyadic congruence
   for \(\sigma\).
2. On each parity separately, \(\sigma/W\) is uniformly distributed in
   \([0,1]\).  In particular there is no uniform positive-proportion
   lower bound.
3. In fact

   \[
      \liminf \sqrt{k}\,\frac{\sigma(k)}{W(k)}=0
   \]

   on each parity.  Thus even a bound of order \(W/\sqrt{k}\) cannot hold
   uniformly.
4. For every fixed \(c>0\), the lower bound

   \[
      \sigma(k)\ge \frac{W(k)}{k^c}
   \]

   does hold on a density-one set in each parity.  This is an almost-all,
   not an all-dimensional, statement.

No numerical search is used.  The only classical analytic inputs are
Stirling's expansion, Weyl's criterion, the van der Corput second-derivative
estimate, and polynomial equidistribution for an irrational leading
coefficient.  The last input uses the irrationality of \(\pi\), but no
irrationality-measure estimate.

---

## 1. One central Wallis quotient controls both parities

Put

\[
 C_m=\binom{2m}{m},
 \qquad
 A_m=\frac{4^m}{2C_m}.
\]

For odd dimension \(k=2m-1\), write a superscript \(-\), and for even
dimension \(k=2m\), write a superscript \(+\).  Then

\[
 W_m^- =\frac{C_m}{2},
 \qquad
 W_m^+=C_m.
\]

Define

\[
 \eta_- =0,
 \qquad
 \eta_+=\frac12,
 \qquad
 y_m^\pm=A_m-\eta_\pm.
\]

### Lemma 1.1 — exact parity unification

For both parities,

\[
 \boxed{\Lambda_m^\pm=W_m^\pm y_m^\pm-1.}
 \tag{1.1}
\]

#### Proof

For \(k=2m-1\), the two central layers have equal size, so

\[
 \Lambda_m^-=2^{2m-2}-1.
\]

Also

\[
 W_m^-A_m
 =\frac{C_m}{2}\frac{4^m}{2C_m}
 =4^{m-1}.
\]

For \(k=2m\), symmetry about the unique central layer gives

\[
 \Lambda_m^+=2^{2m-1}-\frac{C_m}{2}-1,
\]

whereas

\[
 W_m^+\left(A_m-\frac12\right)
 =2^{2m-1}-\frac{C_m}{2}.
\]

These are exactly (1.1).  \(\square\)

---

## 2. Exact quotient-remainder law

Fix either parity and suppress the superscript.  Write

\[
 \Lambda=qW+\rho,
 \qquad 0\le \rho<W,
 \qquad T_t=\binom{t+1}{2}.
\]

Stirling's formula gives \(q=O(\sqrt m)\), while \(W\) is exponential in
\(m\).  Hence \(T_{q+1}<W\) for all sufficiently large \(m\).

### Lemma 2.1 — the two exact cases

For all sufficiently large \(m\),

\[
 (d,\sigma)=
 \begin{cases}
   (q,\ T_q-\rho),&\rho\le T_q,\\[1mm]
   (q+1,\ W-\rho+T_{q+1}),&\rho>T_q.
 \end{cases}
 \tag{2.1}
\]

In particular

\[
 0\le \sigma<W+d.
 \tag{2.2}
\]

#### Proof

At \(t=q\), the defining inequality is precisely \(T_q\ge\rho\).
At \(t=q+1\), it always holds because \(W-\rho+T_{q+1}>0\).
Finally, for \(t=q-1\), the deficit is

\[
 \Lambda-\bigl((q-1)W+T_{q-1}\bigr)
 =W+\rho-T_{q-1}>0.
\]

Thus only \(q\) and \(q+1\) are possible, and substitution gives (2.1).
The previous value of the scalar expression differs from the current one
by \(W+d\), which also gives (2.2).  \(\square\)

---

## 3. Exact dyadic granularity

Let \(s_2(m)\) be the number of ones in the binary expansion of \(m\), and
put

\[
 a_m=s_2(m),
 \qquad
 g_m=2^{a_m-1}.
 \tag{3.1}
\]

Kummer's theorem gives

\[
 v_2(C_m)=s_2(m).
 \tag{3.2}
\]

### Theorem 3.1 — slack congruence

For both parities and every nondegenerate \(m\),

\[
 \boxed{
 \sigma_m^\pm\equiv T_{d_m^\pm}+1\pmod {g_m}.
 }
 \tag{3.3}
\]

Consequently zero slack requires

\[
 \boxed{g_m\mid T_{d_m^\pm}+1.}
 \tag{3.4}
\]

If \(r_m\) denotes the least positive integer congruent to
\(T_d+1\pmod {g_m}\) (with \(r_m=g_m\) when the residue is zero), then

\[
 \sigma_m^\pm>0\quad\Longrightarrow\quad \sigma_m^\pm\ge r_m.
 \tag{3.5}
\]

#### Proof

Write \(C_m=2^{a_m}u_m\) with \(u_m\) odd.  In odd dimension,

\[
 A_m=\frac{2^{2m-1-a_m}}{u_m}
\]

is in lowest terms, and

\[
 \frac{W_m^-}{u_m}=2^{a_m-1}=g_m.
\]

In even dimension,

\[
 A_m-\frac12
 =\frac{2^{2m-a_m}-u_m}{2u_m}
\]

is in lowest terms: its numerator is odd and is coprime to \(u_m\).  Again

\[
 \frac{W_m^+}{2u_m}=2^{a_m-1}=g_m.
\]

Thus in either parity the integer \(W y\) is a multiple of \(g_m\).
By (1.1),

\[
 \Lambda\equiv-1\pmod {g_m}.
\]

Since \(g_m\mid W\), the definition
\(\sigma=dW+T_d-\Lambda\) gives (3.3).  The remaining assertions are
immediate.  \(\square\)

This congruence is an exact all-dimensional obstruction, but its scale is
at most polynomial in \(m\); it does not give a positive fraction of \(W\).

---

## 4. Exact zero and fixed-small-slack equations

Let

\[
 P_d=d(d+1)+2=2(T_d+1).
\]

### Proposition 4.1 — exponential Diophantine form

For any integer \(s\ge0\), the equation \(\sigma=s\) is equivalent to

\[
 \boxed{
 2^{2m-1}=dC_m+P_d-2s
 }
 \tag{4.1-}
\]

in odd dimension, and to

\[
 \boxed{
 2^{2m}=(2d+1)C_m+P_d-2s
 }
 \tag{4.1+}
\]

in even dimension.

In particular, \(\sigma=0\) satisfies these equations with \(s=0\), as
well as the necessary dyadic condition (3.4).

#### Proof

Substitute

\[
 \Lambda_m^-=2^{2m-2}-1,
 \qquad W_m^-=C_m/2
\]

or

\[
 \Lambda_m^+=2^{2m-1}-C_m/2-1,
 \qquad W_m^+=C_m
\]

into \(dW+T_d-\Lambda=s\), then multiply by two.  \(\square\)

The known positive-depth zero-slack cases fit these identities exactly:

\[
 (k,m,d)=(6,3,1),\qquad (9,5,2).
 \tag{4.2}
\]

Indeed \(C_3=20\) makes (4.1+) equal to \(64=3\cdot20+4\), and
\(C_5=252\) makes (4.1-) equal to \(512=2\cdot252+8\).  This is direct
verification, not an exhaustive classification.

### Proposition 4.2 — at most one solution at fixed \((d,s)\)

Fix a parity, \(d\), and \(s\), with \(P_d-2s>0\).  Then (4.1-) or
(4.1+), respectively, has at most one solution \(m\).

Consequently:

1. at each fixed depth and parity there is at most one zero-slack
   dimension;
2. for every fixed \(S\), the number of dimensions \(k\le K\) with
   \(\sigma(k)\le S\) is \(O_S(\sqrt K)\).

#### Proof

Set

\[
 R_m=\frac{4^m}{C_m}.
\]

The central-binomial recurrence gives

\[
 \frac{R_{m+1}}{R_m}=\frac{2(m+1)}{2m+1}>1,
 \tag{4.3}
\]

so \(R_m\) is strictly increasing, whereas \(C_m\) is strictly
increasing.  Dividing (4.1-) and (4.1+) by \(C_m\) gives respectively

\[
 R_m=2d+\frac{2(P_d-2s)}{C_m},
 \tag{4.4-}
\]

and

\[
 R_m=2d+1+\frac{P_d-2s}{C_m}.
 \tag{4.4+}
\]

The left side increases strictly and the right side decreases strictly,
so equality occurs at most once.

For fixed \(S\), only finitely many \(d\), depending on \(S\), have
\(P_d-2s\le0\) for some \(s\le S\).  They contribute only a constant,
because \(d(m)\to\infty\).  All remaining \((d,s)\) contribute at most
one solution per parity.  Finally \(d(m)=\Theta(\sqrt m)\), so only
\(O(\sqrt K)\) depths occur below \(K\).  \(\square\)

This sparsity statement does **not** prove that there are only finitely many
zero-slack dimensions.  Such a claim would require solving, or uniformly
excluding solutions of, (4.1-) and (4.1+) as \(d\to\infty\).

---

## 5. Normalized slack is uniformly distributed

Stirling's expansion gives

\[
 A_m
 =\frac{\sqrt{\pi m}}2
   \left(1+\frac1{8m}+O(m^{-2})\right).
 \tag{5.1}
\]

Let

\[
 x_m^\pm=\frac{\Lambda_m^\pm}{W_m^\pm}
          =A_m-\eta_\pm-\frac1{W_m^\pm},
 \qquad
 \theta_m^\pm=\{x_m^\pm\}.
\]

### Lemma 5.1 — square-root equidistribution

For every nonzero real \(\alpha\), the sequence

\[
 \{\alpha\sqrt m+\beta\}_{m\ge1}
\]

is uniformly distributed modulo one.

#### Proof sketch

By Weyl's criterion it suffices, for each fixed nonzero integer \(h\), to
show

\[
 \sum_{m\le M}e^{2\pi i h\alpha\sqrt m}=o(M).
\]

On a dyadic interval \([N,2N]\), the phase has second derivative of size
\(\asymp_{h,\alpha}N^{-3/2}\).  The van der Corput second-derivative
estimate is therefore \(O_{h,\alpha}(N^{3/4})\).  Summing dyadic intervals
gives \(o(M)\).  Adding a perturbation tending to zero does not alter
uniform distribution.  \(\square\)

Equation (5.1) and Lemma 5.1 show that both \(\theta_m^-\) and
\(\theta_m^+\) are uniformly distributed.

### Theorem 5.2 — paritywise slack equidistribution

Separately for odd and even dimensions, the sequence

\[
 \boxed{S_m^\pm=\frac{\sigma_m^\pm}{W_m^\pm}}
 \]

has the uniform limiting distribution on \([0,1]\).  Explicitly, for
every interval \([a,b]\subset(0,1)\), the proportion of indices with
\(S_m^\pm\in[a,b]\) tends to \(b-a\), and the proportion outside every
fixed neighbourhood of \([0,1]\) tends to zero.  (Individual values can
exceed one by \(O(m/W)\), so this empirical formulation is slightly more
precise than saying that every term lies in \([0,1]\).)

In particular,

\[
 \liminf_{m\to\infty}S_m^\pm=0,
 \qquad
 \limsup_{m\to\infty}S_m^\pm=1.
 \tag{5.2}
\]

#### Proof

Use Lemma 2.1.  Outside the exceptional case

\[
 E_m=\{\theta_m\le T_q/W\},
\]

we have

\[
 S_m=1-\theta_m+O(m/W).
 \tag{5.3}
\]

On \(E_m\), instead \(0\le S_m=O(m/W)\).  The exceptional set has
natural density zero: for every fixed \(\varepsilon>0\), it is eventually
contained in \(\{\theta_m\le\varepsilon\}\), whose upper density tends to
\(\varepsilon\) by uniform distribution; now let \(\varepsilon\downarrow0\).

Thus, for every continuous test function, replacing \(S_m\) by
\(1-\theta_m\) changes its Cesaro average by \(o(1)\).  The latter sequence
is uniformly distributed, proving the claim.  \(\square\)

### Corollary 5.3 — density-one polynomial lower bounds

For every fixed \(c>0\), in each parity the set

\[
 \left\{m:\ \sigma_m^\pm<\frac{W_m^\pm}{m^c}\right\}
 \tag{5.4}
\]

has natural density zero.

#### Proof

By (2.1), condition (5.4) places \(\theta_m\) in shrinking neighbourhoods
of either zero or one.  For every fixed \(\varepsilon>0\), those
neighbourhoods are eventually contained in
\([0,\varepsilon]\cup[1-\varepsilon,1]\).  Uniform distribution bounds the
upper density by \(2\varepsilon\); let \(\varepsilon\downarrow0\).  \(\square\)

---

## 6. Even \(W/\sqrt{k}\) fails uniformly

The preceding equidistribution only gives \(o(W)\) subsequences.  A second
argument gives a quantitative obstruction at the square-root scale.

Squaring the two-term Stirling expansion yields

\[
 A_m^2
 =\frac\pi4\left(m+\frac14+\frac1{32m}+O(m^{-2})\right).
 \tag{6.1}
\]

### Theorem 6.1 — square-root-scale liminf

On each parity,

\[
 \boxed{
 \liminf_{m\to\infty}\sqrt m\,\frac{\sigma_m^\pm}{W_m^\pm}=0.
 }
 \tag{6.2}
\]

#### Proof

Let \(\eta=0\) in odd dimension and \(\eta=1/2\) in even dimension.  For
integers \(n\), put

\[
 \ell_n=n+\eta,
 \qquad
 u_n=\frac{4\ell_n^2}{\pi}-\frac14.
\]

The sequence \(\{u_n\}\) is uniformly distributed modulo one by Weyl's
polynomial theorem, because its quadratic coefficient \(4/\pi\) is
irrational.

Choose any sequence \(\varepsilon_j\downarrow0\).  Uniform distribution
allows increasing \(n_j\) with

\[
 \varepsilon_j\le\{u_{n_j}\}\le2\varepsilon_j.
\]

Put \(m_j=\lfloor u_{n_j}\rfloor\), choosing \(n_j\) large enough that the
error terms below are smaller than \(\varepsilon_j/2\).  Equation (6.1)
gives

\[
 \ell_{n_j}^2-A_{m_j}^2
 =\frac\pi4
   \left(\{u_{n_j}\}-\frac1{32m_j}+O(m_j^{-2})\right)>0,
\]

and hence

\[
 0<\ell_{n_j}-A_{m_j}
 =O\left(\frac{\varepsilon_j}{\sqrt{m_j}}\right).
 \tag{6.3}
\]

Thus \(x_{m_j}=A_{m_j}-\eta-1/W\) lies immediately below the integer
\(n_j\).  It is in the second case of (2.1), and therefore

\[
 \frac{\sigma_{m_j}}{W_{m_j}}
 =n_j-x_{m_j}+O(m_j/W_{m_j})
 =O\left(\frac{\varepsilon_j}{\sqrt{m_j}}\right).
\]

Multiplication by \(\sqrt{m_j}\) and passage to the limit proves (6.2).
\(\square\)

Consequently there is no absolute \(c_0>0\) for which

\[
 \sigma(k)\ge c_0\frac{W(k)}{\sqrt{k}}
\]

holds in every sufficiently large dimension.  The same is automatically
true for every proposed lower bound larger than that scale, such as
\(c_0W/k^a\) with \(a<1/2\).

The theorem does **not** rule out a uniform lower bound
\(W/k^a\) for some \(a>1/2\).  No such all-dimensional bound is proved
here.

---

## 7. Consequences for rounding and additive error

Assume the zero-rank-leakage face of the current lower-deck identity, so
that

\[
 M=D-\sigma,
 \qquad M\ge0.
 \tag{7.1}
\]

There are three distinct quantities that must not be conflated.

### 7.1 Total duplicate count

The total duplicate count necessarily satisfies

\[
 D\ge\sigma.
\]

Since \(\sigma/W\) is uniformly distributed, \(\sigma=\Theta(W)\) on a
positive-density set.  Therefore a global assertion

\[
 D=o(W/k^c)
\]

for the **total** duplicate count is incompatible with (7.1).  The natural
rounding target is not small \(D\); it is small excess \(D-\sigma\).

### 7.2 Excess duplicates or missing targets

If a rounding theorem gives

\[
 D\le\sigma+E(k),
\]

then it gives exactly \(M\le E(k)\).  An estimate
\(E(k)=o(W/\operatorname{poly}(k))\) is still generally unbounded and does
not imply \(B(k)+O(1)\).  For the present terminal theorem one needs
\(E(k)=O(1)\), or a separate absorber that reduces \(E(k)\) to \(O(1)\).

### 7.3 An independent upper bound on total \(D\)

Hypothetically, if one had an all-dimensional lower bound

\[
 \sigma\ge c_0W/k^a
\]

and an independently constructed state with

\[
 D=o(W/k^a),
\]

then eventually \(D\le\sigma\); combined with (7.1), this would force exact
closure.  Likewise \(D=O(W/k^c)\) would suffice if \(c>a\).

But Theorem 6.1 rules out this strategy for every \(a\le1/2\), and no
uniform polynomial lower bound with \(a>1/2\) is established.  Corollary
5.3 makes the comparison valid only on a density-one set, which is
insufficient for an all-dimensional \(B(k)+O(1)\) theorem.

---

## 8. What irrationality estimates do and do not give

It is tempting to use a finite irrationality measure for \(\pi\) to lower
bound the distance from \(A_m\) to the relevant integer or half-integer.
A finite Stirling truncation does not justify that conclusion.

After \(J\) correction terms, solving the truncated expansion for \(\pi\)
produces a rational of denominator polynomial in \(m\), but the omitted
Stirling remainder is also only polynomially small.  Standard
irrationality-measure lower bounds are smaller than this truncation error
and therefore cannot see an exponentially small fluctuation in the exact
rational number \(A_m\).

Accordingly, this note uses only the qualitative irrationality of \(\pi\)
in Theorem 6.1.  It makes no claim that known irrationality measures imply
an all-dimensional polynomial lower bound for \(\sigma/W\).  Excluding all
future zero or exceptionally small slacks remains the exponential
Diophantine problem (4.1-)/(4.1+), not a consequence proved here from
Stirling's formula.

---

## Final verdict

The strongest proof-safe all-dimensional statement obtained here is the
exact arithmetic dichotomy

\[
 \boxed{
 \sigma=0
 \quad\text{or}\quad
 \sigma\ge r_m,
 \qquad
 \sigma\equiv T_d+1\pmod {2^{s_2(m)-1}}.
 }
\]

In relative terms this is only polynomial-over-exponential.  There is no
uniform positive-proportion bound, and even \(cW/\sqrt{k}\) fails
infinitely often.  Polynomial lower bounds hold for density one, but that
does not close an all-dimensional construction.

Therefore the additive-constant programme should target the exact excess

\[
 D-\sigma=M,
\]

not hope that a merely sublinear total leave will automatically fit inside
an always-large scalar slack.
