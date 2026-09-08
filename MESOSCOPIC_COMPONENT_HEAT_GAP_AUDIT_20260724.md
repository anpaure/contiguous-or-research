# Audit: mesoscopic component heat-gap reduction

Date: 2026-07-24

## Verdict

The exact component-switching construction, the two-child heat identity,
and the implication `(HG_L for every fixed L) => MWB` are correct.  Every
child in the argument is one integral exact wreath factor.

One proof sentence needs correction: a generic gap-two Robin Hood transfer
does not necessarily reduce balanced overload by one.  The claimed
inequality `O_q<=Phi_q` remains true and follows directly from the exact
integer deviation decomposition below.

No supplied argument proves `(HG_L)`.  That inequality is the entire new
gate: compare coherent global displacement with incoherent component noise
inside the exact-factor fibre.

## 1. Collision excess dominates overload

Write `W=cN+r`, and put

\[
D=\sum_S(c-\mu(S))_+,
\qquad
E=\sum_S(\mu(S)-c-1)_+.
\]

For pair-collision excess

\[
\Phi=P-P^{\rm bal},
\qquad
P=\sum_S\binom{\mu(S)}2,
\]

one has the exact identity

\[
2\Phi=\sum_S(\mu(S)-c)(\mu(S)-c-1).
\]

If `mu=c-d`, its summand is `d(d+1)>=2d`; if
`mu=c+1+e`, its summand is `e(e+1)>=2e`.  The two balanced values contribute
zero.  Hence

\[
\Phi\ge D+E\ge\max(D,E)=O.
\]

This proves the desired inequality without making a false claim about the
effect of each individual Robin Hood move.

Equivalently, for `lambda=c+alpha`,

\[
2\Phi=|\boldsymbol\mu-\lambda\mathbf1\|_2^2
-N\alpha(1-\alpha).
\]

## 2. Legal switching cube

For exact factors `F,G`, form the bipartite ownership graph whose edges are
middle sets.  It is `n`-regular.  In every connected component, choosing all
factor vertices on either the `F` side or the `G` side selects exactly one
endpoint of every ownership edge.  Independent component-side choices
therefore produce another exact factor.

For `G=sigma F`, let `delta_(K,q)` be the change of the depth-`q` load vector
on component `K`.  If `epsilon_K` records the selected side, then the child
load is

\[
\frac{\mu_q(F)+\mu_q(\sigma F)}2
+\frac12\sum_K\epsilon_K\delta_{K,q}.
\]

No fractional object is emitted; averaging is used only to prove that one
integral sign choice is good.

## 3. Exact heat identity

Define

\[
A_H=\sum_{q\le H}\frac{
\|\mu_q(F)-\mu_q(\sigma F)\|_2^2}{c_q},
\]

\[
R_H(\epsilon)=\sum_{q\le H}\frac{
\|\sum_K\epsilon_K\delta_{K,q}\|_2^2}{c_q},
\]

and

\[
\Psi_H(F)=\sum_{q\le H}\frac{\Phi_q(F)}{c_q}.
\]

The parallelogram identity, together with the factor-independent floor in
the Euclidean representation of `Phi_q`, gives exactly

\[
\Psi_H(F_\epsilon)+\Psi_H(F_{-\epsilon})
=2\Psi_H(F)+\frac14(R_H(\epsilon)-A_H).
\]

For independent uniform signs,

\[
\mathbb E R_H(\epsilon)
=V_H:=\sum_{q\le H}\frac1{c_q}
\sum_K\|\delta_{K,q}\|_2^2,
\]

and therefore

\[
\boxed{
\mathbb E\Psi_H(F_\epsilon)
=\Psi_H(F)-\frac18(A_H-V_H).
}
\]

The constants `1/4` and `1/8` are correct.

## 4. Continuous smoothing versus integral noise

For a uniformly random coordinate permutation, transitivity and zero total
mass of the centered load imply

\[
\mathbb E_\sigma
\|x_q-\sigma x_q\|_2^2=2\|x_q\|_2^2
\ge4\Phi_q(F).
\]

Thus

\[
\mathbb E_\sigma A_H(F,\sigma)\ge4\Psi_H(F).
\]

This is only continuous/global smoothing.  Since

\[
A_q=\left\|\sum_K\delta_{K,q}\right\|_2^2,
\qquad
V_q=\sum_K\|\delta_{K,q}\|_2^2,
\]

their gap is the sum of cross-component inner products.  It can have either
sign.  A bound on `A_H` alone says nothing sufficient about `A_H-V_H`.

## 5. Exact sufficient lemma

For fixed `L`, set `H=ceil(L sqrt(m))`.  It is enough to prove that every
exact factor admits a coordinate permutation with

\[
\boxed{
A_H(F,\sigma)-V_H(F,\sigma)
\ge\eta_L\Psi_H(F)-C_LH\operatorname{Cat}_m
}
\tag{HG_L}
\]

for some positive finite constants depending only on `L`.

The heat identity then gives a deterministic integral child satisfying the
contracting recurrence

\[
\Psi_{t+1}\le(1-\eta_L/8)\Psi_t
+(C_L/8)H\operatorname{Cat}_m.
\]

Iteration reaches

\[
\Psi_H=O_L(H\operatorname{Cat}_m)=o(W)
\]

for fixed `L`.  Since `O_q<=Phi_q`, this proves the fixed-window MWB target.
Diagonalizing over integer `L` gives a slowly growing
`omega(m)->infinity`, with `omega=o(sqrt(m))`, and hence full MWB.

## Remaining problem

Prove `(HG_L)`, or a multistep analogue using nonlocal factor-fibre
circuits.  Spectral smoothing of `A_H`, fractional averaging, and finite
positive gaps below the first shadow do not control `V_H` uniformly.  The
additive `H Cat_m` term is deliberately large enough to absorb the discrete
integer floor and a Catalan-scale first-shadow obstruction; what is missing
is a theorem that no larger component-noise obstruction persists for an
appropriate legal coupling.
