# Self-audit: MLD birth configurations, chainization, and weighted Hall

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_MLD_BIRTH_CONFIGURATION_CHAINIZATION_AND_WEIGHTED_HALL_GATE_20260805.md`  
**Method:** pure mathematical replay; no computation, search, or solver  
**Verdict:** GO after scope corrections.  The birth-refinement, literal
chainization, generalized-Hoelder moment bound, geometric weight estimate,
and Hall exponent are correct.  The theorem is unconditional for an
unconditioned sequence of independent uniform augmented Boolean matchings.
Its exceptional-bank and protected-carrier consequences remain explicitly
conditional.

## 1. Configuration-at-birth quantifiers

At the interface from rank `b-1` to rank `b`, the old image has the fixed
size `binom(k,b-1)`.  Hence the newborn cohort has deterministic size

\[
 {k\choose b}-{k\choose b-1}.
\]

After deleting the empty set, the one transported singleton and all
rank-one newborns have the same residual length and may be merged.  Their
merged size is `binom(k,1)`.  Thus every cohort size used in the theorem is
deterministic.

The MLD refinement theorem applies exactly under the following order of
quantifiers:

1. configuration menus and integer cell sizes are fixed from deterministic
   cohort/resource data;
2. conditional on the current cohort, its fixed-size refinement is uniform;
3. every future augmented Boolean matching is independent and uniform.

The choice may not inspect an individual realised path or its future
geometry.  Refining only the newborn row is allowed: give every old row its
identity transition and apply the cohortwise refinement theorem.  At rank
one, first merge the two MLD labels and then refine the merged class.

The audited theorem now states these quantifiers explicitly.  Its phrase
"physically legitimate" was weakened to "probabilistically legitimate":
the refinement assigns abstract future-role data, but does not itself expose
a socket or prove compatibility with a protected carrier.

## 2. MLD role unions at every rank

A path born at rank `b` has the deterministic rank sequence

\[
 b,b+1,\ldots,t.
\]

A composition of its length therefore fixes every fragment-top rank before
the path's sets are known.  For fixed `(s,v)`, define the deterministic
label set

\[
 J_{s,v}=\{(b,p):p\text{ has a mark-}v\text{ piece ending at rank }s\}.
\]

At rank `s`, the named top family is literally the union of current MLD
cells indexed by `J_(s,v)`.  Positive composition parts give distinct
endpoints, so one path contributes at most once at a fixed rank.  Cutting
the disjoint Boolean paths consequently partitions every ordinary target
exactly once into consecutive inclusion chains.

For every deterministic `B subset binom([k],s)`, MLD gives

\[
 \mathbb E e^{\theta|Q_{s,v}\cap B|}
 \le(1-p_{s,v}+p_{s,v}e^\theta)^{|B|},
 \qquad
 p_{s,v}={|Q_{s,v}|\over{k\choose s}}.
\]

The class sizes, hence `|Q_(s,v)|`, are deterministic.  Differentiating at
zero gives the exact mean.  No independence between different ranks or
different marks is asserted or needed.

## 3. Extreme-point exception count

For `N` jobs and `D` aggregate socket-tail inequalities, restrict a feasible
extreme point to its positive support.  The support matrix has rank at most
`N+D`, so it has at most `N+D` positive variables.  Every job contributes
at least one.  If `f` jobs have two or more positive configurations, then
the support has at least `N+f` variables, whence

\[
                              f\le D.
\]

Every other job has one positive variable, equal to one.  Retaining those
configurations can only decrease each nonnegative socket-tail use.
Interchangeability within one birth-length cohort converts the retained
jobs to deterministic counts suitable for uniform refinement.

The bound depends on the number of aggregate resource rows, not on the
name `D` by itself.  If further configuration labels impose `R` additional
independent aggregate constraints, the proof gives at most `D+R`
exceptions (or the rank of all active non-job rows).  The theorem was
patched to prevent the former overbroad reading.

## 4. Generalized Hoelder and sub-Poisson MGF

For positive weights `a_i`, let

\[
 A=\sum_i a_i,
 \qquad
 \gamma_i={a_i\over A}.
\]

Generalized Hoelder with exponents `1/gamma_i` gives

\[
 \mathbb E e^{\lambda\sum_i a_iX_i}
 \le\prod_i
   (\mathbb E e^{\lambda A X_i})^{\gamma_i}
 \le
 \exp\left({\mu\over A}(e^{\lambda A}-1)\right),
\]

because `sum gamma_i mu_i=mu/A`.  Centering and using

\[
 e^x-1-x\le{x^2\over2(1-x/3)}
 \qquad(0\le x<3)
\]

produces a sub-gamma variable with variance proxy `A mu` and scale `A/3`:

\[
 \Pr(Z-\mu\ge g)
 \le\exp\left(-{g^2\over2(A\mu+Ag/3)}\right).
\]

Only one-dimensional upper MGFs are used, so arbitrary cross-rank
dependence is harmless.  In the application, the binomial MLD bound implies
the required sub-Poisson estimate via `log(1+x)<=x`.

## 5. Exact means and geometric weight sum

For fixed `v,T` and `1<=s<=t`, put

\[
 X_s=|Q_{s,v}\cap\tbinom Ts|,
 \qquad
 a_s={1\over{k-s\choose v-s}}.
\]

The flag identity

\[
 {{v\choose s}\over{k-s\choose v-s}}
 ={{k\choose s}\over{k\choose v}}
\]

shows term by term that

\[
 \mathbb E(a_sX_s)={|Q_{s,v}|\over{k\choose v}}.
\]

Summing gives the exact mean `m_v/binom(k,v)`.

The largest weight occurs at `s=t`, and

\[
 {a_{s-1}\over a_s}
 ={v-s+1\over k-s+1}\le{2\over3}
\]

for `2<=s<=t`, `v<=ceil(k/2)`; when `t=1` the following bound is
immediate.  Therefore

\[
 \sum_{s=1}^t a_s
 \le {3\over{k-t\choose v-t}}
 ={3\over d_v}.
\]

There is no hidden rank-zero term: the empty set was deleted before
fragmentation.  The theorem now treats `t=0` as a separate vacuous case.

## 6. Hall exponent and union-bound constant

Assume `H_v>0` and `0<=m_v<=H_v`, put

\[
 \Delta_v=H_v-m_v,
 \quad
 \mu={m_v\over{k\choose v}},
 \quad
 g={\Delta_v\over{k\choose v}}.
\]

Both `mu` and `g` are at most `H_v/binom(k,v)`.  Substitution of
`A<=3/d_v` into the Hoelder tail gives

\[
 \Pr\left(Z_v(T)>{H_v\over{k\choose v}}\right)
 \le
 \exp\left(-{\Delta_v^2d_v
                  \over8{k\choose v}H_v}\right).
\]

This constant is safe (using `m_v+Delta_v=H_v` would improve it slightly).
The number of owner tests is at most

\[
 \sum_v{k\choose v}\le2^k.
\]

Consequently the explicit sufficient condition

\[
 {Delta_v^2d_v\over{k\choose v}H_v}\ge A_0k
\]

works for any fixed `A_0>8 log 2`.  The theorem was patched from the less
literal notation `Omega(k)` to this exact form.  Once every pointwise bound
holds, the cited fractional-matching/integrality theorem supplies distinct
collar starts.

## 7. Physical scope

The proof does not establish any of the following:

* compatibility of the unconditioned independent matching law with a
  central owner chronology, upper-window coverage, or residence;
* preservation of MLD after conditioning on protected edges, sockets,
  endpoints, or upper witnesses;
* physical occurrence-faithful exposure of the maximum-capacity exceptional
  bank;
* attachment of the exceptional paths' named tops; or
* the same `D`-exception bound after adding further constrained resource
  rows to the configuration LP.

The conditional final implication was patched to require both physical
bank exposure and valid named-top attachment.  Its “no prescribed-top
extension problem” conclusion is now explicitly limited to the ordinary,
unconditioned lower bulk.

## 8. Final status

The following chain is proved:

\[
 \boxed{
 \begin{gathered}
 \text{independent uniform Boolean interfaces}
 +\text{cohort-uniform birth configurations}\\
 \Longrightarrow\text{literal target-once ordinary chains with MLD tops},\\
 \text{MLD tops}+\text{reserve (5.12)}
 \Longrightarrow\text{exact ordinary top-to-collar matching}.
 \end{gathered}}
\]

Fractional feasibility with exactly `D` aggregate tail rows adds at most
`D` exceptional paths.  Closing those exceptions and coupling the lower
construction to the protected upper/resident carrier remain physical
premises.  No all-dimensional universal-word or `B(k)+O(1)` conclusion is
proved here.
