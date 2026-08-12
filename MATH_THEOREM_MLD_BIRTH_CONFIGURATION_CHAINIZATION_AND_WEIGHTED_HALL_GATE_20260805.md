# MLD birth configurations give literal target-once chains and close the weighted Hall sum

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional lower-side probabilistic theorem, with an
explicit conditional Hall/absorber consequence.  Starting from independent
uniform augmented Boolean matchings, whole fragmentation configurations
whose eligibility depends only on deterministic birth-cohort data may be
assigned uniformly inside each chain-birth cohort and carried to the cutoff
without losing multinomial Laplace domination.  This produces literal
target-once fragmented inclusion chains.  Generalized Hölder combines the
exact one-rank Laplace bounds and closes the complete weighted multi-rank
Hall sum at the sharp variance scale.  A configuration LP with exactly `D`
aggregate resource rows leaves at most `D` exceptional chains.  The theorem
does not prove that this unconditioned path-cover law coexists with a
protected upper/resident carrier, nor does it physically expose the
exceptional socket bank.

## 1. The uncoloured Boolean path cover

Fix a dimension `k` and a cutoff `1<=t<ceil(k/2)`.  The case `t=0` is
empty after deleting the empty set and is vacuous.  Between every consecutive
pair of complete ranks `q,q+1`, independently choose a uniform perfect
matching in the augmented Boolean interface: every old rank-`q` set is
matched upward and the remaining rank-`q+1` sets are matched to universal
start dummies.

The resulting directed edges form pairwise disjoint inclusion paths which
cover every set of ranks `0,...,t`.  After deleting the empty set, they
partition the nonempty lower ideal into chains

\[
 S_b\subset S_{b+1}\subset\cdots\subset S_t.
\tag{1.1}
\]

All paths born at rank `b` have the same residual job length

\[
 L_b=t-b+1.
\tag{1.2}
\]

At rank one, merge the unique continuation of the empty set with the
rank-one newborns; all of them have the same nonempty residual length.
Thus the deterministic birth-cohort sizes are

\[
 H_1={k\choose1},
 \qquad
 H_b={k\choose b}-{k\choose b-1}\quad(2\le b\le t).
\tag{1.3}
\]

The cohort-stable Boolean theorem implies that the partition of every
current rank by path-birth/history labels has multinomial Laplace
domination (`MLD`).

## 2. Assign complete configurations at birth

For length `L`, let `mathcal P_L` be any finite family of literal
fragmentation configurations.  A configuration `p` specifies

* a composition of `L` into positive piece lengths;
* for every piece, a collar/socket mark `v` whose physical capacity is at
  least that piece length;
* any further future role label drawn from an admissible menu which is
  identical for every path of length `L` in that birth cohort.

For each birth rank `b`, fix nonnegative integers

\[
 n_{b,p}\quad(p\in\mathcal P_{L_b}),
 \qquad e_b\ge0,
 \qquad
 \sum_pn_{b,p}+e_b=H_b,
\tag{2.1}
\]

where `H_b` is the deterministic number of paths in that birth class and
`e_b` is an exceptional count.  At the moment the cohort is born, refine
it uniformly into cells of these sizes.  For the merged rank-one cohort,
perform the same refinement after the merge.

The families `mathcal P_(L_b)` and all counts in (2.1) must be fixed from
deterministic cohort/resource data before the realised birth positions and
before every future interface matching.  They may not be selected after
inspecting an individual path.  In particular, every member of one cohort
must have the same literal eligibility menu for the labels being assigned.

### Theorem 2.1 (configuration-labelled path MLD)

At every later rank, the partition of active paths by the complete labels
`(b,p)` and the exception labels is MLD.  Every union of configuration
labels therefore has the exact binomial Laplace benchmark on every
deterministic family of current-rank vertices.

#### Proof

The newborn cohort is part of an MLD partition by the cohort-stable
Boolean transport theorem.  Uniform fixed-count refinement inside that
cohort preserves MLD, including arbitrary structural zeros in the
birth-to-configuration matrix.  Every later independent augmented Boolean
matching transports the labels and adds the next newborn cohort while
preserving MLD.  At rank one, merging the transported-empty and newborn
labels is MLD-preserving before the common refinement.  Induction over the
ranks proves the claim. `square`

This refinement is probabilistically legitimate under the stated
eligibility hypothesis: eligibility depends only on the already known
birth rank, the common terminal cutoff, and other deterministic cohort
data, so every member of one refined cohort has exactly the same menu.  No
refinement by realised path geometry is used.  This does not itself expose
a literal socket or certify compatibility with a separately protected
carrier.

## 3. Literal target-once fragmentation

For each ordinary path, cut its sequence (1.1) according to its assigned
configuration.  Let `Q_(s,v)` be the rank-`s` targets which are tops of
pieces carrying socket mark `v`.

### Theorem 3.1 (target-once and one-rank spread)

The ordinary fragments are pairwise target-disjoint consecutive inclusion
chains.  Together they cover every target on every ordinary path exactly
once.

Moreover, for every fixed `(s,v)`, the family `Q_(s,v)` is a union of
current configuration labels.  Put

\[
 p_{s,v}={|Q_{s,v}|\over {k\choose s}}.
\tag{3.1}
\]

For every deterministic `B subset binom([k],s)` and every real `theta`,

\[
 \boxed{
 \mathbb E e^{\theta|Q_{s,v}\cap B|}
 \le(1-p_{s,v}+p_{s,v}e^\theta)^{|B|}.}
\tag{3.2}
\]

In particular the mean is exactly `p_(s,v)|B|`, and the ordinary binomial
Chernoff--Bernstein bounds hold.

#### Proof

Cutting disjoint paths partitions them into disjoint subpaths, proving the
first assertion.  Whether configuration `(b,p)` has a marked-`v` piece top
at rank `s` is deterministic, so `Q_(s,v)` is a union of labels.  Apply
MLD and merge all labels in that union. `square`

Thus the named-target extension problem is gone: the target names were
fixed by the paths before the socket marks were inspected.

## 4. Exact anonymous configuration rounding

Suppose the whole-job configuration LP for the birth-length multiset is
feasible against socket tails `(K_q)_(q<=D)`, and that these are its only
aggregate resource rows besides the one equality for each job.  The basic
configuration rounding theorem gives deterministic counts `(n_(b,p))`
satisfying (2.1) such that

\[
 \sum_be_b\le D
\tag{4.1}
\]

and the ordinary configurations use no more than the original socket
tails.

#### Justification

Take an extreme point of the job-specific configuration LP.  At most `D`
jobs have more than one positive configuration.  Retain the unique
integral configuration of every other job and count retained configurations
within each birth class.  Jobs of one birth class are interchangeable, so
these counts may be assigned by the uniform refinement in Section 2.
The discarded jobs give `(e_b)` and (4.1).  If the configuration LP has
`R` additional independent aggregate resource rows for further role
labels, the same argument gives only `D+R` exceptions (more precisely, at
most the rank of all active non-job rows).  Merely writing an extra role
label into a configuration does not preserve the `D` bound when that label
also carries a new constrained resource.

Consequently fractional configuration feasibility has now been converted
to

* exact literal fragmentation of all but at most `D` paths;
* exact socket-tail compliance for those ordinary fragments;
* an MLD-spread named top family;
* at most `D` exceptional whole paths requiring a separate absorber.

## 5. The weighted multi-rank Hall row closes by generalized Hölder

For a socket mark whose collar rank is `v`, a fixed owner
`T in binom([k],v)` sees normalized request load

\[
 Z_v(T)=
 \sum_{s<v}{|Q_{s,v}\cap\binom Ts|
             \over {k-s\choose v-s}}.
\tag{5.1}
\]

Its exact mean follows from (3.2) and flag counting:

\[
 \boxed{
 \mathbb EZ_v(T)
 ={m_v\over{k\choose v}},
 \qquad
 m_v=\sum_s|Q_{s,v}|.}
\tag{5.2}
\]

Indeed,

\[
 {{v\choose s}\over{k-s\choose v-s}}
 ={{k\choose s}\over{k\choose v}}.
\tag{5.3}
\]

If, simultaneously for every `T`,

\[
 Z_v(T)\le {H_v\over{k\choose v}},
\tag{5.4}
\]

then the exact pointwise codegree theorem matches all ordinary fragment
tops to distinct collar starts.

### Theorem 5.1 (Hölder--MLD weighted Bernstein inequality)

Let `(X_i)` be arbitrary, possibly dependent, nonnegative random variables
with exact means `mu_i` and binomial Laplace domination

\[
 \mathbb Ee^{\tau X_i}
 \le\exp\bigl(\mu_i(e^\tau-1)\bigr)
 \qquad(\tau\ge0).
\tag{5.5}
\]

For positive weights `(a_i)`, put

\[
 Z=\sum_i a_iX_i,
 \qquad
 \mu=\mathbb EZ=\sum_i a_i\mu_i,
 \qquad
 A=\sum_i a_i.
\tag{5.6}
\]

Then

\[
 \boxed{
 \mathbb Ee^{\lambda(Z-\mu)}
 \le
 \exp\left({\mu\over A}
 (e^{\lambda A}-1-\lambda A)\right)}
 \qquad(\lambda\ge0),
\tag{5.7}
\]

and hence

\[
 \boxed{
 \Pr\{Z-\mu\ge g\}
 \le
 \exp\left(-{g^2\over2(A\mu+Ag/3)}\right)}.
\tag{5.8}
\]

#### Proof

Put `gamma_i=a_i/A`.  Generalized Hölder, with conjugate exponents
`1/gamma_i`, gives

\[
 \begin{aligned}
 \mathbb Ee^{\lambda Z}
 &=\mathbb E\prod_i e^{\lambda a_iX_i}\\
 &\le\prod_i
   \left(\mathbb Ee^{\lambda a_iX_i/\gamma_i}\right)^{\gamma_i}\\
 &=\prod_i
   \left(\mathbb Ee^{\lambda AX_i}\right)^{\gamma_i}\\
 &\le
 \exp\left((e^{\lambda A}-1)\sum_i\gamma_i\mu_i\right)\\
 &=\exp\left({\mu\over A}(e^{\lambda A}-1)\right).
 \end{aligned}
\tag{5.9}
\]

Multiply by `e^(-lambda mu)` to obtain (5.7).  The standard inequality
`e^x-1-x<=x^2/(2(1-x/3))` for `0<=x<3`, followed by Chernoff
optimization, gives (5.8). `square`

No independence across ranks was used.

### Theorem 5.2 (sharp ordinary-top Hall concentration)

For the statistic (5.1), put

\[
 d_v={k-t\choose v-t},
 \qquad
 \Delta_v=H_v-m_v.
\tag{5.10}
\]

Assume `t<v<=ceil(k/2)`, `H_v>0`, and `0<=m_v<=H_v`.  Then for every
owner `T`,

\[
 \boxed{
 \Pr\left\{Z_v(T)>{H_v\over{k\choose v}}\right\}
 \le
 \exp\left(-{\Delta_v^2d_v\over8{k\choose v}H_v}\right).}
\tag{5.11}
\]

Consequently there is an absolute `A_0` such that every ordinary top is
simultaneously matchable whenever every `Delta_v>0` and

\[
 \boxed{
 {\Delta_v^2d_v\over{k\choose v}H_v}\ge A_0k
 }
\tag{5.12}
\]

#### Proof

For fixed `(s,v,T)`, Theorem 3.1 and (3.2) give (5.5) for

\[
 X_s=|Q_{s,v}\cap\tbinom Ts|,
 \qquad
 \mu_s=p_{s,v}{v\choose s}.
\tag{5.13}
\]

Apply Theorem 5.1 with

\[
 a_s={1\over{k-s\choose v-s}}.
\tag{5.14}
\]

Only the nonempty ranks `1<=s<=t` occur.  For `2<=s<=t`, the ratio

\[
 {a_{s-1}\over a_s}={v-s+1\over k-s+1}\le {2\over3}
\tag{5.15}
\]

for the relevant middle-lower range, and hence (with the case `t=1`
immediate)

\[
 A=\sum_sa_s\le {3\over d_v}.
\tag{5.16}
\]

Equation (5.2) gives `mu=m_v/binom(k,v)`.  In (5.8), take

\[
 g={\Delta_v\over{k\choose v}}.
\tag{5.17}
\]

Both `mu` and `g` are at most `H_v/binom(k,v)`.  Substitution of (5.16)
into (5.8) gives (5.11).  There are at most

\[
                         \sum_v{k\choose v}\le2^k
\]

pairs `(v,T)`.  Thus any fixed `A_0>8\log2` makes (5.12) and the union
bound force all inequalities (5.4) with positive probability. `square`

Thus, for the unconditioned birth-refined lower construction, neither
arbitrary persistent-colour assignment nor cross-rank independence remains
as a probabilistic gate.  This statement does not survive arbitrary
geometry-dependent conditioning without a separate proof.

## 6. Exceptional paths

Assume `D>=1`; when `D=0` the intended positive-job system is vacuous.
The at most `D` exceptions in (4.1) contain at most `D L_max` targets and
can be fragmented by the universal auxiliary bank of

\[
 D\left\lceil{L_{\max}\over D}\right\rceil
\tag{6.1}
\]

maximum-capacity sockets.  This is a polynomial-size bank in the Boolean
application.  A complete all-dimensional construction still has to expose
that bank occurrence-faithfully and attach its named tops.  The existing
one-depth insurance calculations show exponential scalar margin, but
capacity-faithful physical exposure is a separate premise.

## 7. Exact consequence and frontier

Combining Sections 1--6 gives the following conditional implication.

> If the all-price fractional configuration inequalities hold, the
> reserve condition (5.12) is available, and the polynomial exceptional
> bank is exposed occurrence-faithfully together with a valid attachment
> of all of its named tops, then
> the complete lower ideal has a literal target-once fragmented-chain lift
> with all collar starts matched.

The remaining upper/carrier requirements—central owner chronology,
arbitrary-width upper coverage, and residence—are not proved here.  Nor is
it proved that conditioning the Boolean matchings to satisfy those
requirements preserves the unconditioned MLD law used above; compatibility
must be obtained by a joint construction or a separate conditioning
theorem.

The gain is a strict reduction of the lower side:

\[
 \boxed{
 \text{fractional configuration}
 +\text{the proved MLD--Hölder lift}
 +\text{a }D\text{-job absorber}.}
\]

For the unconditioned ordinary lower bulk there is no longer a separate
prescribed-top extension problem, newborn-cohort accumulation, arbitrary
persistent-colour matching oracle, or multi-rank independence assumption.
The exceptional bank and the protected upper/resident carrier remain
physical gates.

## 8. Dependencies

1. `MATH_THEOREM_BOOLEAN_COHORT_STABLE_MULTINOMIAL_LAPLACE_INDUCTION_20260805.md`;
2. `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`;
3. `MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`.
