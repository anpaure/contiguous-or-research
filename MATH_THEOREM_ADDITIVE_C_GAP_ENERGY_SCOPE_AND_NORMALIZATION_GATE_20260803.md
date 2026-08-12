# Additive-constant gap energy: the fixed-depth theorem extends, but arbitrary near-optimal words require a normalization theorem

**Date:** 2026-08-03  
**Status:** unconditional for the stated run-system / fixed-depth carrier
hypotheses; explicit obstruction to inferring those hypotheses from an
arbitrary universal word of length `B(k)+C`. No computation is used.

## 0. Outcome

Put

\[
r=\left\lceil\frac k2\right\rceil,
\quad W=\binom kr,
\quad \Lambda=\sum_{s=1}^{r-1}\binom ks,
\quad M=\sum_{s=1}^{r-1}s\binom ks,
\]

and let `d=d(k)` be least with

\[
dW+\binom{d+1}{2}\ge\Lambda.
\]

Fix a constant `C>=0`, and write

\[
e=d+C,\qquad E=e+1,
\qquad \epsilon_k=\frac{dW-\Lambda}{W}.
\tag{0.1}
\]

If a length-`W+e` construction is obtained by cutting a complete resident
cyclic rank-`r` Johnson carrier at **fixed depth `e`**, then the multi-rail
gap theorem remains valid verbatim with `d` replaced by `e`. In particular,
bounded lower defect forces

\[
\boxed{
\frac{P}{rW}\ge
\frac{4}{8-\pi+8(\epsilon_k+C)}-o(1)
\ge
\frac{4}{16-\pi+8C}-o(1),
}
\tag{0.2}
\]

where `P` is the total coordinatewise source-occurrence count in the
erosion supports. Thus `P=Omega_C(rW)`, and a fixed number of sparse
residue rails still fails.

The zero-deletion extreme also still fails: full depth-`e` erosion omits
asymptotically at least

\[
\boxed{2\Phi(-\sqrt{\pi/2})=0.210\ldots}
\tag{0.3}
\]

of the strict lower ideal. A fixed additive `C` does not change this limit.

These conclusions do **not** presently apply to every arbitrary universal
word of length `W+d+C`. The architecture-free endpoint theorem supplies
variable rank-`r` witness intervals of length at most `d+C+1`; it does not
supply one rank-`r` owner at every start, Johnson adjacency, a fixed-depth
row identity, or residence. Those are exactly the hypotheses used by gap
energy.

## 1. The weakest run-system form of gap energy

The local identity needs no cyclic symmetry and no Johnson labels. Consider
any collection of positive coordinate runs, unwrapped as integer intervals.
For a run of owner length `L>=E`, let its admissible source interval have
the two mandatory endpoints and span `L-E`. Choose retained occurrence
markers containing those endpoints, with successive gaps

\[
1\le g\le E.
\]

For `1<=q<=e`, count the length-`q` source cells meeting a retained marker
inside this run. Exactly as in the cyclic proof,

\[
\sum_{q=1}^{e}H_q(L)
=e\left(L-\frac E2\right)-\sum_g\binom g2.
\tag{1.1}
\]

Suppose the run system has:

* total positive owner mass `L_tot`;
* `R` positive runs;
* `P` retained coordinatewise markers.

If different run hulls of one coordinate are disjoint for all cell lengths
at most `e`, summing (1.1) gives the exact linear-run identity

\[
\boxed{
H=U-J,
\quad U=e\left(L_{\rm tot}-\frac{RE}{2}\right),
\quad J=\sum_g\binom g2,
}
\tag{1.2}
\]

and

\[
G:=\#\{g\}=P-R,
\qquad
S:=\sum_g g=L_{\rm tot}-RE.
\tag{1.3}
\]

Consequently

\[
J\ge\frac12\left(\frac{S^2}{P-R}-S\right)
\tag{1.4}
\]

when `S>0`.  When `S=0`, every admissible source interval is a singleton,
`P=R`, and the exact convention is `J=0`; no quotient by `P-R` is used.
If `B_exc` additional short cells lie outside these run-local
cells, and every represented strict-lower target is assigned injectively
to a cell whose rank is at most its signature rank, then defect `delta`
satisfies

\[
M-\delta(r-1)
\le U-J+(r-1)B_{\rm exc}.
\tag{1.5}
\]

Equations (1.2)--(1.5) are the weakest variable-window version: they require
only a run decomposition, separated eroded hulls, mandatory endpoints,
bounded occurrence gaps, and signature domination of assigned cell values.
They do not require cyclicity.

If

\[
L_{\rm tot}=rW+O_C(r),
\quad R=W+O_C(1),
\quad
B_{\rm exc}=\binom E2+O_C(E),
\tag{1.6}
\]

then the extra-run and boundary terms change the rank ledger by only
`O_C(k^{3/2})` beyond the standard boundary allowance. The standard
boundary itself contributes `O(k^2)`. Both are negligible compared with
`M=Theta(kdW)`. Hence the same positive linear-density conclusion (0.2)
follows. This prices a bounded number of extra owners, cuts, or boundary
strips exactly at the scale needed for an additive constant.

## 2. Exact fixed-depth-`e` theorem

For a complete cyclic rank-`r` Johnson carrier with residence floor `E`,

\[
L_{\rm tot}=rW,\qquad R=W.
\]

The linear cut contributes at most

\[
B_e=\binom E2
\]

extra short cells. Thus define

\[
U_e=We\left(r-\frac E2\right),
\qquad
S_e=W(r-E),
\]

and

\[
K_e=U_e+(r-1)B_e-M+\delta(r-1).
\tag{2.1}
\]

Whenever a lower assignment of defect at most `delta` exists,

\[
\boxed{
P\ge W+\frac{S_e^2}{S_e+2K_e}.
}
\tag{2.2}
\]

This is the exact finite additive-`C` density bound.

At central rank and bounded `delta`, replacing `d` by `e=d+C` leaves
`e^2/k -> pi/8`, while

\[
\frac{eW-\Lambda}{W}=\epsilon_k+C.
\]

The parity-specific rank calculation therefore gives

\[
\frac{K_e}{kW}
=\frac{4-\pi}{16}+\frac{\epsilon_k+C}{2}+o(1),
\qquad
\frac{S_e}{kW}=\frac12+o(1).
\tag{2.3}
\]

Substitution into (2.2) proves the first inequality in (0.2). Minimality
of `d` gives the sharper exact bounds

\[
-\frac{\binom{d+1}{2}}{W}\le \epsilon_k
<1-\frac{\binom d2}{W}.
\tag{2.4}
\]

In particular `-o(1)<=epsilon_k<1`.  Since the first right-hand side in
(0.2) decreases with `epsilon_k+C`, this proves the uniform second
inequality.

A union of `h` exact minimum nets or canonical residue rails has

\[
\frac{P}{rW}\le\frac{h}{e}(1+o(1)).
\]

Hence any bounded-defect such system needs `h=Omega_C(e)=Omega(d)`;
every fixed `h` fails.

For full erosion, all cyclic lower cells have rank at least `r-e`.
Even granting the boundary cells arbitrary values, the defect is at least

\[
\left[
\sum_{s=1}^{r-e-1}\binom ks-\binom E2
\right]_+.
\tag{2.5}
\]

Since `C` is fixed,

\[
\frac{r-e-1-k/2}{\sqrt{k}/2}
\longrightarrow-\sqrt{\pi/2}.
\]

Since `Lambda/2^k -> 1/2` and `binom(E,2)=O(k)`, the central limit
theorem applied to (2.5) gives, explicitly,

\[
\frac{\left[\sum_{s=1}^{r-e-1}\binom ks-\binom E2\right]_+}
{\Lambda}
\longrightarrow 2\Phi(-\sqrt{\pi/2}),
\]

which proves (0.3).

## 3. Why an arbitrary `B(k)+C` word does not yet inherit the theorem

Let `A_1,...,A_(W+e)` be an arbitrary universal word. The endpoint-chain
theorem gives `W` selected rank-`r` witness intervals with distinct right
endpoints and lengths at most `e+1`. It also gives a strong aggregate
recency estimate. It does **not** give:

1. a row `T_1,...,T_W` with one owner at every consecutive start;
2. the fixed-depth identity
   \[
   T_i=A_i\cup\cdots\cup A_{i+e};
   \]
3. Johnson adjacency, hence exactly one run birth per owner transition;
4. total positive-run count `W+O_C(1)`;
5. residence floor `e+1` and separated erosion hulls.

Without items 3--5, the identities `R=W`, `L_tot=rW`, and (1.2) cannot be
inserted into the rank ledger. In particular, a variable-witness system may
have many coordinate births at one transition, and its run count need not
be `W+O(C)`.

There is a concrete obstruction to the naive normalization.  In every
dimension with `W>1` in which a flat depth-`d` universal factor exists,
start from such a factor and append one arbitrary nonempty letter.
Universality is preserved and the length is `W+d+1`.  In the resulting
word, the first `W-1` entries of the depth-`(d+1)` row are unaffected by
the appended boundary letter and are the adjacent unions

\[
D^{d+1}A^+=D(D^dA)=DT,
\]

where `A^+` denotes the appended word and the displayed identity is read
on those first `W-1` entries,

which have rank `r+1` along a simple Johnson carrier, not rank `r`. Thus

\[
\text{universal of length }B(k)+1
\centernot\Longrightarrow
\text{complete flat rank-}r\text{ row at depth }d+1.
\tag{3.1}
\]

This does not refute the possibility of a different normalization; it
shows that such a normalization is an additional theorem, not a consequence
of length and universality alone.

## 4. Precise remaining normalization gate

To promote (0.2) to every additive-constant word, it is enough to prove:

> **Additive-constant resident row normalization.** From every universal
> word of length `W+d+C`, extract or transform, without increasing lower
> defect by more than `O_C(1)`, a run system satisfying (1.6), separated
> depth-`e` erosion hulls, mandatory endpoints, and signature domination of
> every transported short-cell witness.

The stronger flat cyclic Johnson normalization is sufficient but not
necessary; the run-system conditions (1.6) are the actual minimum input to
gap energy.

Until such a theorem is proved, the proof-safe conclusion is:

\[
\boxed{
\begin{array}{c}
\text{every fixed-depth resident }B(k)+C\text{ construction requires}
\ P=\Omega_C(rW),\\
\text{but this has not yet been derived from an arbitrary universal}
\ B(k)+C\text{ word.}
\end{array}}
\]
