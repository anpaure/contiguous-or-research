# Pair codegrees and random-packing barrier for monotone queue atoms

## 1. Verdict

The monotone-profile queue atom has an excellent same-rank pair codegree but
a larger, unavoidable cross-depth codegree.

For one fixed rank row, two masks at Johnson distance `r` have exact
normalized codegree

\[
 {2(a_q-r)\over a_q
   {m-q\choose r}{m+q\choose r}},
\]

with the obvious interchange of `m-q,m+q` for the two rank signs.  The
largest same-row ratio is `Theta(m^(-2))`.

Across adjacent depths, nested masks exposed at the same center have
normalized codegree `Theta(m^(-1))`.  Thus the full-band atom hypergraph has
maximum normalized codegree at least order `1/m`, while a typical edge has
order `m^(3/2)` vertices for the proposed depth range.  In particular,

\[
  |E_{\rm atom}|\,{\Delta_2\over\Delta_1}
       =\Omega(\sqrt m).
\]

This does not prove that a specially correlated packing is impossible, but
it prevents a black-box inference from small pair codegree.

Independent random queues fail much more decisively.  With `W/H` independent
atoms, the expected duplicate mass is

\[
   \left({\sqrt\pi\over e}+o(1)\right)W\sqrt m,
\]

and already the middle row alone has `(e^(-1)+o(1))W` duplicates with
probability `1-exp(-Omega(W/H))`.  Therefore independent sampling, followed
by deletion of collisions, cannot prove the required `o(W)` duplicate bound.

The remaining lemma is a high-precision, quota-respecting correlated packing
theorem.  Ordinary random queues do not supply it, and a standard
fixed-uniformity nibble cannot simply be cited because the edge size grows and
an `o(total band size)` leftover is still too weak by a factor `sqrt(m)`.

## 2. One random queue

Put `n=2m` and take the proposed choice `H=m-h`.  The queue then uses exactly
`2m` distinct coordinates and is a uniformly random permutation.

Fix a profile and let `a_q` be the number of centers which reach depth `q`.
For either rank sign, the exposed masks at depth `q` are `a_q` consecutive
intervals of one fixed length

\[
                         k=m-q\quad\hbox{or}\quad k=m+q
\]

in that random permutation.  Translating all interval starts by the fixed
sign-dependent offset has no effect on the following count.

For a fixed `k`-set `S`, exactly `a_q k!(n-k)!` permutations place `S` in
one of the allowed intervals.  Hence

\[
             \Pr(S\hbox{ occurs})={a_q\over {n\choose k}}.
                                                               \tag{2.1}
\]

After averaging over the profile distribution,

\[
        \mathbb E a_q=H{{n\choose m-q}\over W},
        \qquad W={n\choose m},
\]

so every band mask has the common marginal probability

\[
                             {H\over W}.             \tag{2.2}
\]

## 3. Exact same-row codegree

Let `S,T` be distinct `k`-sets at Johnson distance

\[
                  r=|S-T|=|T-S|.
\]

Because the interval starts are consecutive and `a_q<=m-q`, both masks can
occur only at starts separated by exactly `r`.  For one orientation and one
pair of starts, the four permutation blocks are

\[
   S-T,\quad S\cap T,\quad T-S,\quad [n]-(S\cup T),
\]

of sizes `r,k-r,r,n-k-r`.  Therefore

\[
 \Pr(S,T\hbox{ both occur})
 ={2(a_q-r)(r!)^2(k-r)!(n-k-r)!\over n!}             \tag{3.1}
\]

when `1<=r<a_q`, and it is zero otherwise.

Dividing by (2.1) gives the exact normalized codegree

\[
 \boxed{
 {\Pr(S,T\text{ both})\over\Pr(S)}
 = {2(a_q-r)\over a_q
       {k\choose r}{n-k\choose r}}.}
                                                               \tag{3.2}
\]

For `k=m+-q` the denominator is

\[
                  {m-q\choose r}{m+q\choose r}.
\]

Uniformly for `q<=h=o(m)` the maximum occurs at `r=1` and is
`(2+o(1))/m^2` whenever `a_q` is not vanishingly small.

## 4. Cross-depth nested codegree

The different ranks are not independent copies of the same-row system.
They are nested suffixes or prefixes of one queue interval.

For example, let `0<=q<r<=h`, put

\[
       k=m-q,\qquad l=m-r,\qquad b=r-q,
\]

and fix masks `T subset S` with `|S|=k,|T|=l`.  The same-center lower-chain
occurrence places the `b` elements of `S-T`, followed by the `l` elements of
`T`, in one interval.  There are `a_r` possible centers, and therefore the
same-center contribution is exactly

\[
 \Pr_{\rm aligned}(S,T)
 ={a_r b!l!(n-k)!\over n!}.                          \tag{4.1}
\]

Relative to the occurrence probability of `S`, this is

\[
 \boxed{
 {\Pr_{\rm aligned}(S,T)\over\Pr(S)}
 ={a_r\over a_q}{1\over{k\choose b}}.}              \tag{4.2}
\]

The upper chains have the identical formula after reversing containment.
For adjacent depths `b=1` and bounded `q`,

\[
       {a_{q+1}\over a_q}{1\over m-q}
                    =(1+o(1)){1\over m}.             \tag{4.3}

There can also be shifted nested placements.  Their number is at most
`b+1`; they change the constant but not the order.  Thus cross-depth pairs
exhibit normalized codegree `Theta(1/m)`, one power of `m` larger than
same-row pairs.

This is a positive correlation forced by the symmetric-chain geometry, not
an artefact of profile rounding.

## 5. Atom size

For one profile the number of exposed band masks is

\[
                  K=a_0+2\sum_{q=1}^h a_q.
\]

Averaging over profiles gives

\[
 {\mathbb E K\over H}
   =1+2\sum_{q=1}^h\rho_q,
 \qquad
 \rho_q={{2m\choose m-q}\over{2m\choose m}}.        \tag{5.1}
\]

For `h=sqrt(m omega)` with `omega->infinity` in the valid moderate-deviation
range,

\[
       1+2\sum_{q=1}^h\rho_q
              =(\sqrt\pi+o(1))\sqrt m.              \tag{5.2}
\]

Hence, with `H=(1-o(1))m`,

\[
                    \mathbb E K=(\sqrt\pi+o(1))m^{3/2}.           \tag{5.3}

Combining (4.3) and (5.3) gives

\[
             K\,{\Delta_2\over\Delta_1}=\Omega(\sqrt m)          \tag{5.4}

for the full-band hypergraph.  The centre-only hypergraph is much better:
it has edge size `H=Theta(m)` and normalized pair codegree
`Theta(m^(-2))`.

Thus choosing disjoint centers is only the first stage.  It does not make
the exposed lower and upper chain masks approximately independent.

## 6. Exact duplicate expectation for independent atoms

Take

\[
                         A=\lfloor W/H\rfloor
\]

independent random queues and independently sampled profiles.  For every
fixed mask in every band row, (2.2) gives

\[
                         X\sim\operatorname{Bin}(A,H/W).
\]

With `lambda=AH/W=1-o(1)`,

\[
 \mathbb E(X-1)_+
 =\mathbb EX-\Pr(X>=1)
 =\lambda-1+(1-H/W)^A
 =e^{-1}+o(1).                                      \tag{6.1}

The total number of masks in the controlled band is

\[
 B_h=W+2\sum_{q=1}^hN_q
    =(\sqrt\pi+o(1))W\sqrt m.                       \tag{6.2}

Linearity of expectation now gives

\[
 \boxed{
 \mathbb E\sum_{q,\,\mathrm{sign}}D_q
    =\left({\sqrt\pi\over e}+o(1)\right)W\sqrt m.}  \tag{6.3}

This is larger than the required `o(W)` by a factor of order `sqrt(m)`.

Already at depth zero,

\[
 \mathbb ED_0
 =AH-W\left(1-(1-H/W)^A\right)
 =(e^{-1}+o(1))W.                                   \tag{6.4}

Changing one atom changes `D_0` by at most `2H`.  McDiarmid's inequality
therefore gives, for a fixed sufficiently small `c>0`,

\[
 \Pr(D_0<cW)
       \le \exp\left(-\Omega(W/H)\right).            \tag{6.5}

Thus the independent construction fails with overwhelming probability, not
merely in expectation.  Deleting one atom for every duplicate loses a
positive fraction of all center mass before the deeper ranks are considered.

## 7. What a nibble would still have to prove

A matching theorem on the centre-only atom hypergraph would remove the
middle-row duplicates.  The corrected packing lemma, however, needs

\[
 D_0+\sum_{q=1}^h(D_q^-+D_q^+)=o(W)
\]

together with every row quota.  This is much stronger than covering a
`1-o(1)` fraction of the full band, whose size is `Theta(W sqrt(m))`:
an `o(B_h)` leftover may still be much larger than `W`.

Moreover the atom uniformity grows as `Theta(m^(3/2))`, and the dangerous
cross-depth codegree ratio is `Theta(1/m)`.  Fixed-uniformity
Pippenger--Spencer theory therefore does not apply verbatim, and no
quantitative growing-uniformity theorem has been supplied whose error is
`o(W/B_h)=o(m^(-1/2))` at these parameters.

This is not an impossibility theorem for correlated queue packings.  It is a
sharp boundary on the probabilistic shortcut:

\[
 \boxed{
 \text{random queues are Poisson-collision dominated; a successful proof
 must correlate atoms simultaneously across all depths.}
 }
\]

