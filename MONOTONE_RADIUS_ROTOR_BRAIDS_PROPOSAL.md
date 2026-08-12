# Monotone-radius rotor braids (submitted proposal; unaudited)

Work on a `2m`-set.  Fix `0<=h<m`, `H<=m-h`, and pairwise distinct
coordinates

\[
 z_{-h},z_{-h+1},\ldots,z_{H+m-1}.
\]

For `0<=t<H`, let

\[
 S_t=\{z_t,z_{t+1},\ldots,z_{t+m-1}\}.
\]

For `0<=d<=h`, define the symmetric chain centered at `S_t` by

\[
 C^{-q}_{t,d}=\{z_{t+q},\ldots,z_{t+m-1}\},\qquad
 C^q_{t,d}=\{z_{t-q},\ldots,z_{t+m-1}\}\quad(0<=q<=d).
\]

Put `L_t^(d)=C^{-d}_{t,d}` and define the ordered partition

\[
 \Pi_t(d)=(L_t^{(d)},\{z_{t+d-1}\},\ldots,\{z_t\},
 \{z_{t-1}\},\ldots,\{z_{t-d}\},R_t^{(d)}),
\]

where `R` contains all remaining coordinates.

## Claimed variable-radius transition

For `0<=e<=d<=h`, append

\[
 X=L_{t+1}^{(e)}=\{z_{t+e+1},\ldots,z_{t+m}\}.
\]

The move-to-front update `M_X(Pi_t(d))` is claimed to have prefix unions
containing `C(t+1,e)`.  For `e<d`, its claimed beginning is

\[
 X,\{z_{t+e}\},\ldots,\{z_{t+1}\},
 \{z_t\},\ldots,\{z_{t+1-e}\},\ldots.
\]

For `e=d`, the residual `L_t^(d) minus X={z_(t+d)}` allegedly supplies the
first singleton after `X`.

## Claimed monotone-profile atom

For `d_0>=d_1>=...>=d_(H-1)`, the chains `C(t,d_t)` are pairwise disjoint and
one MTF path exposes them successively.  Initializing `Pi_0(d_0)` by writing
its nonempty blocks in reverse order is claimed to cost at most `2d_0+2`
entries; subsequent updates cost one each, giving word length at most

\[
 H+2d_0+1.
\]

## Fractional profile claim

Let

\[
 W={2m\choose m},\qquad N_q={2m\choose m-q},\qquad \rho_q=N_q/W.
\]

For one atom with `H` starts choose integers

\[
 H=a_0>=a_1>=...>=a_h>=0,
\]

and define `d_t=max{q:t<a_q}`.  Exactly `a_q` centers reach depth `q`.  The
real vector `(H rho_1,...,H rho_h)` lies in the integral monotone polytope,
so there is a profile distribution with `E a_q=H rho_q`.

Take every injective coordinate queue uniformly and independently sample the
profile.  By coordinate symmetry a rank `m+-q` mask is claimed to have
expected incidence `(H rho_q)/N_q=H/W` per unit atom weight.  Giving all
atoms total fractional mass `W/H` therefore covers every central-band mask
exactly once, with total center mass `W` and reset mass at most

\[
 (W/H)(2h+1).
\]

The proposed asymptotic choice is

\[
 h=\lceil\sqrt{m\omega(m)}\rceil,\qquad H=m-h,
\]

where `omega(m)->infinity` and `omega(m)=o(m)`.  Then reset mass is claimed
`o(W)` and the outside binomial tails are claimed `o(W)`.

## Integral gate

For an integral atom family, let `mu_q(S)` count occurrences of rank
`m+-q` target `S` and

\[
 D_q=\sum_S(\mu_q(S)-1)_+.
\]

If profile quotas have total depth-`q` incidences
`N_q+O(W/H)`, the number missing at depth `q` is claimed at most
`D_q+O(W/H)`, and hence

\[
 Q<=\sum_{q=0}^h D_q+O(hW/H).
\]

The missing packing lemma asks for `W/H+o(W/H)` integral atoms with

\[
 \sum_{q=0}^hD_q=o(W).
\]

Together with literal missing masks and outside tails, this is claimed to
imply `nu(2m)<=W+o(W)`.

This file records the submitted proposal for audit; it is not a certified
theorem note.
