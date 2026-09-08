# Audit and synthesis: the sharp independent reservoir versus SCD tails

## Verdict

The submitted independent-reservoir theorem is mathematically valid.  Its
leading cutoff

```text
q_0=(1+o(1)) sqrt(m log log m)
```

is sharp for the stated class of independent uniformly random queue atoms
whose total number of starts is `o(W)`.  The concentration argument in the
submitted Theorem 3 is also valid.  Two presentational refinements are useful:

1. the displayed assertion `E Q_*=W m^(1/2-o(1))` needs both the proved lower
   bound and the immediate upper bound `E Q_*<=sum_q N_q`; and
2. `Pr(Q_*=o(W))->0` means that for every deterministic `a_m=o(W)`,
   `Pr(Q_*<=a_m)->0`.

There is, however, an important synthesis correction.  Once the exact
symmetric-chain-product (SCD) tail word is available, the random reservoir no
longer gives the best outer cutoff.  The SCD word alone covers all depths at
least `sqrt(m) omega(m)`, for an arbitrarily slowly diverging `omega`, at
`o(W)` cost.  Since `sqrt(m log log m)/sqrt(m)->infinity`, placing an SCD tail
at the reservoir cutoff covers everything that the reservoir and its literal
tail covered, without using any random atoms.  Thus the reservoir theorem is
a sharp theorem about its mechanism, but it does **not** improve the current
best combined gate.

No coefficient-one conclusion follows: the interval between the exact shallow
cover and an arbitrary `sqrt(m) omega(1)` cutoff is still open.

## 1. Audit of the constructive reservoir theorem

For a fixed signed depth `q`, a fixed-radius atom with `H` starts contains
exactly `H` distinct masks in that rank.  Coordinate transitivity therefore
gives the exact one-atom hit probability

```text
H/N_q.
```

For `p` independent atoms and `pH>=W/g`, a fixed target is missed with
probability at most

```text
exp(-1/(g rho_q)),   rho_q=N_q/W.
```

The exact binomial ratio satisfies

```text
rho_q=product_{i<q}(m-i)/(m+i+1)
     <=exp(-q^2/(m+q)).
```

Hence the submitted choice

```text
q_0^2/(m+q_0)>=log(g(1+epsilon)log m)
```

makes every target beyond `q_0` fail with probability at most
`m^(-(1+epsilon))`.  Summing over fewer than `2m` signed rows proves the
displayed `2m^(-epsilon)W` repair bound.

With `H=floor(m/log m)` and reservoir radius
`R=sqrt((1/2+2epsilon)m log m)+O(1)`, one has `R/H=o(1)`, so the atom words
cost `(1+o(1))W/g`.  The geometric binomial-tail estimate is also correct:

```text
2 sum_{q>R}N_q/W
 <=O(m/R) exp(-(R+1)^2/(m+R+1))
 =o(1).
```

Finally, `log g=o(log log m)` implies

```text
log(g(1+epsilon)log m)=log log m+o(log log m),
```

so the asserted leading cutoff follows uniformly over the admitted `g`.

## 2. Audit of the lower bound and concentration

Put

```text
q_*=(1-delta)sqrt(m log log m)+O(1),
Delta=floor(m/(10q_*)).
```

Uniformly for `q_*<=q<=q_*+Delta`, the change in `q^2/m` is `O(1)` and
`q^3/m^2=o(1)`.  Expanding the exact product gives

```text
rho_q=(log m)^(-(1-delta)^2+o(1)).
```

Let the independent atoms have deterministic start counts `H_j<=m`, total
`T=sum_j H_j=o(W)`, and arbitrary deterministic radius profiles.  A fixed
rank-`m-q` target is hit by atom `j` with probability at most `H_j/N_q`.
Since `N_q` is exponential,

```text
log Pr(target missed)
 >=-T/N_q-2 sum_j H_j^2/N_q^2
 =-o(log m).
```

The last equality uses `(1-delta)^2<1`, `T=o(W)`, and
`sum H_j^2<=mT`.  Thus every target is missed with probability `m^(-o(1))`.
There are `Delta=m^(1/2-o(1))` rows and each contains
`W(log m)^(-(1-delta)^2+o(1))` targets, proving the lower bound

```text
E Q_*>=W m^(1/2-o(1)).
```

The reverse inequality follows immediately from
`Q_*<=sum_{q=q_*}^{q_*+Delta}N_q`, so the broad exponent notation in the
submitted equality is justified.

Resampling atom `j` changes the missing count in each row by at most `H_j`
(the submitted `2H_j` is a harmless relaxation), hence changes `Q_*` by at
most `2Delta H_j`.  McDiarmid gives

```text
Pr(Q_*<=E Q_*/2)
 <=exp(-(E Q_*)^2/(2Delta^2 sum_j H_j^2))
 <=exp(-W/m^(1+o(1)))=o(1).
```

Consequently `Q_*>>W` with high probability.  This proves the claimed
mechanism-specific sharpness.

## 3. The exact miss ledger and an optimized cutoff equation

The union bound can retain the rank factor `rho_q` instead of replacing
`N_q` by `W`.  For reservoir radius `R`, the exact expectation bound is

```text
E M_[q0,R]/W
 <=2 sum_{q=q0}^R rho_q exp(-1/(g rho_q)).              (3.1)
```

Let `u>0`, and choose `q_0` so that

```text
q_0^2/(m+q_0)>=log(gu).                                (3.2)
```

Then `rho_q<=1/(gu)` and `1/(g rho_q)>=u` for every `q>=q_0`.
Since `z -> z exp(-1/(gz))` is increasing,

```text
E M_[q0,R]/W
 <=2(R-q_0+1) e^(-u)/(gu).                             (3.3)
```

Thus, for any desired normalized repair budget `eta_m`, it is enough to take
`u=u_m` satisfying

```text
u_m e^(u_m)>=2(R+1)/(g eta_m),                         (3.4)
```

and then use (3.2).  Equivalently,
`u_m` may be the principal Lambert-W value
`W_0(2(R+1)/(g eta_m))`.

For a polynomial-scale radius with
`log R=(1/2+o(1))log m`, and any subpolynomially small repair budget for which
`log(1/eta_m)=o(log m)`, equation (3.4) gives

```text
u_m=(1/2+o(1))log m,
log(gu_m)=log log m+log g-log 2+o(1).
```

This improves the submitted sufficient exponent `(1+epsilon)log m` to the
natural half-logarithmic scale after the row sizes are retained.  It changes
only second-order terms in `q_0`; under `log g=o(log log m)` one still has

```text
q_0=(1+o(1))sqrt(m log log m).
```

## 4. Valid reservoir--SCD splice, and why it is dominated

Let `R<=m/2`, `R/H=o(1)`, and `R/sqrt(m)->infinity`.  Concatenating

1. the random fixed-radius atoms covering depths `q_0,...,R`,
2. literal repairs for the misses in (3.1), and
3. the exact SCD product word `T_(m,m-R-1)` covering depths `R+1,...,m`,

gives the rigorous finite/asymptotic bound

```text
L_outer
 <=(W/g)(1+(2R+1)/H)+o(W)
   +2W sum_{q=q0}^R rho_q exp(-1/(g rho_q))
   +L_m(m-R-1).                                      (4.1)
```

Here `L_m(m-R-1)=o(W)` by the audited SCD theorem.  Taking, for example,
`H=floor(m/log m)` and `R=sqrt(m) omega(m)` with
`omega->infinity` and `omega=o(sqrt(m)/log m)` makes the traversal and SCD
terms `o(W)`; (3.2)--(3.4) control the repair term.

However, if `q_0/sqrt(m)->infinity`, the same SCD theorem may simply be
applied with excluded half-width `q_0` (with the harmless one-rank shift
dictated by the chosen convention).  It then covers **all** depths at least
`q_0` at `o(W)` cost, without the reservoir.  More generally, for every
arbitrarily slowly diverging `omega`, the SCD word alone begins at

```text
sqrt(m) omega(m),
```

which can be asymptotically smaller than `sqrt(m log log m)`.

Therefore the strongest current synthesis is:

```text
exact shallow cover through o(sqrt(log m))
   + unresolved annulus
   + SCD tails beginning at sqrt(m) omega(1).
```

The upper edge of the unresolved annulus is `sqrt(m) omega(1)`, not
`(1+o(1))sqrt(m log log m)`.  The independent-reservoir result remains useful
as a sharp characterization of that random mechanism, but it is superseded
for the global OR construction by deterministic SCD tails.
