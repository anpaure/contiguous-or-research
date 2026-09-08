# The one missing theorem for the coefficient-one asymptotic

## Mesoscopic weighted-wreath balancing problem

For `m>=1`, put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q}.
\]

For a cyclic order `pi` of `[n]`, let `I_pi(j,r)` be its cyclic interval of
length `r` starting at `j`.

An **exact middle wreath factor** is a family `F_m` of `W/n` cyclic orders
such that the `W` sets

\[
\{I_\pi(j,m):\pi\in F_m,\ j\in\mathbb Z_n\}
\]

are precisely all `m`-subsets of `[n]`, each once.

At depth `q>=1`, define the load of an `(m-q)`-set `S` by

\[
\mu_q(S)=
\#\{(\pi,j):\pi\in F_m,\ I_\pi(j,m-q)=S\}.
\]

There are exactly `W` occurrences at every depth.  Put

\[
c_q=\left\lfloor\frac{W}{N_q}\right\rfloor.
\]

A balanced quota vector at depth `q` assigns to each `S` one of the two
values `c_q,c_q+1`, with total quota exactly `W`.  Define the minimum balanced
overload

\[
O_q(F_m)=
\min_b\sum_{S\in\binom{[n]}{m-q}}
       (\mu_q(S)-b(S))_+,
\]

where the minimum is over balanced quota vectors `b`.

### Required theorem

Prove that there are a function `omega(m)->infinity`, with
`omega(m)=o(sqrt(m))`, and exact middle wreath factors `F_m` such that, for

\[
H_m=\left\lceil\sqrt m\,\omega(m)\right\rceil,
\]

one has

\[
\boxed{
\sum_{q=1}^{H_m}
\frac{O_q(F_m)}{c_q}=o(W).
}
\tag{MWB}
\]

The construction and estimate must hold simultaneously across all depths in
one integral factor.  A fractional factor, independent random occupancy
model, or a separately chosen factor for each `q` does not satisfy the
statement.

## Why this completes the proof

Let `M_q` be the number of sets with `mu_q(S)=0`.  For a minimizing balanced
quota vector, total underload equals total overload.  Every hole has quota at
least `c_q`, so

\[
M_q\le \frac{O_q(F_m)}{c_q}.
\]

Thus (MWB) gives `sum_{q<=H_m} M_q=o(W)`.

The already proved literal wreath-transfer word then covers the complete
central band, repairing lower holes and their complementary upper holes, in
length

\[
W+\frac{2H_m+1}{n}W+2\sum_{q=1}^{H_m}M_q=W+o(W).
\]

The already proved symmetric-chain-product tail word covers every remaining
rank in `o(W)` length because `H_m/sqrt(m)->infinity` and `H_m=o(m)`.
Consequently

\[
\nu(2m+1)\le W+o(W).
\]

Sperner gives the reverse bound, and the trimmed one-coordinate lift transfers
the result to even dimensions.  Hence (MWB) implies

\[
\boxed{\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.}
\]

## Stronger but simpler acceptable target

It is enough, though stronger than (MWB), to construct exact factors with

\[
\sum_{q=1}^{H_m}
\#\{S\in\tbinom{[n]}{m-q}:\mu_q(S)=0\}=o(W).
\]

This raw-hole version is easier to state but discards the useful Gaussian
capacity discount in (MWB).
