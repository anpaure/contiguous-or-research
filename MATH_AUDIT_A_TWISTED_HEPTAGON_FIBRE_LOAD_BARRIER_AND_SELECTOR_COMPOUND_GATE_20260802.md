# Twisted-heptagon fibre loads: the moving-skeleton barrier and the selector-compound gate

**Date:** 2026-08-02  
**Lane:** A, independent bounded-load audit  
**Status:** exact negative result for a fixed rooted twisted-geodesic fibre;
exact load ledger for the raw central projection; conditional sharp replacement
criterion.  This note does not assert that the replacement selector compound
exists.

## 0. Outcome

The prospective count

\[
 {r-1\choose 6}{k-r-1\choose 6}(7!)^2\,\Omega(k)^7       \tag{0.1}
\]

cannot be used as the completed-ticket abundance of one protected
Pascal/pull-ear task.  The two factors have different quantifiers.

* The binomial product counts different rank-`r` owner anchors `X` through
  one named cyclic boundary coordinate.
* The completed-ticket interface fixes the private rooted task `(X,a)`, the
  coprime step `h`, and an admitted boundary state `omega`.
* After `X` and `h` are fixed, the moving geodesic has at most `(7!)^2`
  ordered skeletons.  Cap labels, backup providers, and protected collars do
  not change that skeleton.

Consequently any fixed-root completed subfamily of size at least `c k^7`
contains one moving skeleton at least `c k^7/(7!)^2` times.  Already its
first intermediate owner, or its first occurrence-labelled directed history
transition, has that load.  This is not `O(k^6)` for fixed constants.

Thus the desired bounded-load theorem is false on the literal fixed-root
twisted atlas unless the entire moving/history skeleton is declared private.
The smallest genuine escape is an additional selector with `Omega(k)`
different moving/history cores for the *same* external rooted task.  One
degree of the seven nominal filler degrees must be spent on this core
selector, leaving `Theta(k^6)` completions per core.  Cap-provider planting
does not supply this missing selector.

## 1. The exact fibre decomposition

Fix an odd `k`, a rank `r`, a coprime step `h`, and a rank-`r` owner `X`
such that

\[
 |X\setminus\rho^hX|=|\rho^hX\setminus X|=7.           \tag{1.1}
\]

Put

\[
 D=X\setminus\rho^hX,\qquad I=\rho^hX\setminus X.     \tag{1.2}
\]

For `sigma in S(D)` and `tau in S(I)`, define the ordered geodesic

\[
 G_{\sigma,\tau}=(x_0,\ldots,x_7),\qquad
 x_j=\bigl(X\setminus\{\sigma_1,\ldots,\sigma_j\}\bigr)
       \cup\{\tau_1,\ldots,\tau_j\}.                  \tag{1.3}
\]

It has `x_0=X` and `x_7=rho^hX`.  There are exactly

\[
                         S=(7!)^2                       \tag{1.4}
\]

ordered skeleton labels.  If a named deleted coordinate is required in the
first deletion position, this only decreases the number to `6!7!`.

For row `j`, put `f_j=x_j\cap x_{j+1}`.  A raw retained extension label lies
in

\[
 Z_j=[k]\setminus(x_j\cup x_{j+1}),\qquad
 |Z_j|=n:=k-r-1.                                      \tag{1.5}
\]

Before the finitely many simplicity exclusions, a skeleton has exactly
`n^7` extension-labelled central tickets.  After any such exclusions it has
at most `n^7`; on the advertised `Omega(k)^7` face it has at least
`c_0 k^7` for some fixed `c_0>0`.

The seven-run composition count

\[
 A_{k,r}={r-1\choose6}{k-r-1\choose6}                  \tag{1.6}
\]

counts possible values of `X` when only a run-boundary coordinate is fixed.
Thus the raw marginal atlas decomposes as

\[
 \mathcal T_{a,h}
   =\coprod_X\coprod_{(\sigma,\tau)\in S_7^2}
       \mathcal T_{X,\sigma,\tau},                    \tag{1.7}
\]

with prospective size `A_(k,r) S Omega(k)^7`.  Equation
(1.7), rather than a single list of that size for a fixed task, is the
load-bearing decomposition.

## 2. Exact central load ledger

First normalize the atlas by retaining at most one physical collar/backup
completion for each central tuple.  Extra completion labels can only increase
loads and are not needed to witness central abundance.

Fix one ordered skeleton and temporarily allow the full product
`Z_0 times ... times Z_6`.  The loads are as follows.

| resource type | load on this skeleton |
|---|---:|
| any moving owner `x_j` | `n^7` |
| any moving facet `f_j` | `n^7` |
| any directed moving event `(x_j,sigma_(j+1),tau_(j+1),x_(j+1))` | `n^7` |
| one row-indexed extension label `z_j=z` | `n^6` |
| one row-indexed retained owner `f_j+z` | `n^6` |
| one row-indexed old or new cap `x_j+z` or `x_(j+1)+z` | `n^6` |
| one row-indexed old or new incidence option determined by `z` | `n^6` |

The first three rows are identities: none of the seven extension choices
changes the moving geodesic.  In each later row the named set or occurrence
fixes the one extension coordinate `z_j`, leaving the other six choices.
For an arbitrary legal subproduct the corresponding upper bound is still
`n^6`.

On the whole fixed-`X` atlas, a literal cap or retained-owner token can occur
in only a constant number of row/skeleton roles, so its normalized central
load is `O(S n^6)=O(k^6)`.  In contrast, a moving-skeleton token has load at
least the size of one skeleton fibre, `Omega(k^7)`.  Therefore the first
failure is not a cap token; it is a moving owner/facet/history event.

This also explains why the marginal factor `A_(k,r)` is misleading.  A fixed
root owner `X` occurs in all `S Omega(k)^7` tickets of its rooted fibre.  If
`X` is declared private, the same conclusion holds for an intermediate
owner or directed event after one skeleton fibre is selected.

## 3. The fibrewise load barrier

Let `omega` be a fixed admitted bi-history state.  Let `C(X,a,h,omega)` be
any family of completed tickets satisfying all literal cap-provider and
collar requirements, and assume that forgetting those auxiliary choices
projects each ticket to one of the skeletons (1.3).

### Theorem 3.1 (fixed-root moving-token barrier)

If

\[
              |C(X,a,h,omega)|\ge c k^7,               \tag{3.1}
\]

then some nonroot intermediate moving owner and some occurrence-labelled
directed moving-history event have load at least

\[
                       {c\over(7!)^2}k^7.               \tag{3.2}
\]

Consequently, for any constants `c,C>0`, the simultaneous bounds

\[
 |C(X,a,h,omega)|\ge c k^7,qquad
 \max_q \deg_C(q)\le Ck^6                              \tag{3.3}
\]

are impossible for all

\[
                         k>{C(7!)^2\over c},            \tag{3.4}
\]

when moving owners or directed moving-history events are counted as
nonanchor resources.  On a quotient-orbit ledger, the owner assertion uses
the usual admissibility hypothesis that the seven moving owner orbits are
distinct; without it the raw socket is not yet a simple quotient packet.
The occurrence-labelled directed-event assertion does not require forgetting
the literal phase occurrence.

#### Proof

Partition the completed family by its ordered skeleton.  There are at most
`S=(7!)^2` parts, so one part has at least `|C|/S` members.  Every member of
that part contains the same first intermediate owner

\[
                 x_1=X-\{\sigma_1\}+\{\tau_1\},        \tag{3.5}
\]

which is different from the root `X`, and the same first directed event.
Their loads are at least `|C|/S`, proving (3.2).  Comparing (3.2) with
`Ck^6` gives (3.4).  Auxiliary cap providers and collars do not enter the
projection and cannot change the conclusion. \(\square\)

The theorem remains true if the history filter accepts only a subset of the
skeletons; replacing `(7!)^2` by the number of accepted skeletons strengthens
the lower bound.  It also remains true if every central tuple has many
provider/collar completions, since all such copies retain the same moving
event.

### Corollary 3.2 (what can be privatized)

Declaring only `(X,a)` or the two-token root skeleton private does not remove
the obstruction.  Declaring the *entire* seven-step moving/facet/history
skeleton private does remove (3.2), but then compatibility of those private
skeletons across tasks is a new skeleton-assignment problem.  The raw count
(0.1) and the local provider theorem do not solve that problem.

## 4. Why the provider theorem does not change the barrier

Let a completed ticket have a protected terminal bank `P` with `L` incidence
edges and let `q` named old caps require backup providers.  The protected
provider theorem gives a literal embedding when

\[
 {m+1-v_O(P)-2q\choose2}>v_F(P)+q,qquad
                         L+2q\le m-2.                   \tag{4.1}
\]

For `L=O(d)`, `q=O(d)`, and `d=o(m)`, the first inequality is automatic for
all sufficiently large `m`; hence the advertised simplified condition
`L+2q<=m-2` is valid asymptotically under those quantifiers.

This theorem proves that each already chosen compatible collar/cap bank can
be planted.  It does not:

1. change the moving geodesic (1.3);
2. produce `Omega(k)` different moving cores for one rooted task;
3. choose provider occurrences equitably across a ticket atlas; or
4. make an exterior history state accepting.

In particular, even granting that every one of `Theta(k^7)` extension
tuples of one skeleton has a legal protected provider completion, the first
event still has load `Theta(k^7)`.

There is a second, independent warning.  Existential provider planting is
not a provider-*load* theorem.  If completed tickets distinguish provider
choices, a canonical choice may itself be used in every ticket.  A balanced
provider assignment must be supplied separately.  The provider clique for
one cap has `binom(m+1,2)` edges, so a balanced assignment can in principle
give edge load `O(M/m^2)` and owner-endpoint load `O(M/m)` for `M` requests;
neither distribution follows merely from (4.1).

## 5. Sharp selector requirement and a sufficient compound interface

The barrier spends exactly one polynomial degree.

### Proposition 5.1 (necessary skeleton diversity)

Let a rooted completed family have size at least `c k^7` and moving-resource
load at most `Ck^6`.  Then it must use at least

\[
                         \left\lceil{c\over C}k\right\rceil  \tag{5.1}
\]

distinct moving skeleton fibres.

#### Proof

Every skeleton fibre contains a fixed directed moving event.  The load bound
permits at most `Ck^6` tickets in a fibre.  Divide the total size by this
quantity. \(\square\)

Thus the minimal replacement is a one-parameter **selector-return
compound**.  A proof-safe sufficient form is the following.

### Theorem 5.2 (conditional selector-compound subatlas)

Fix one external rooted task `(X,a,omega)`.  Suppose there is a selector set
`J` and completed variant families `V_j`, `j in J`, with constants
`alpha,beta,B,mu,G>0` independent of `k`, such that:

1. `|J|>=alpha k`;
2. every `V_j` has `beta k^6<=|V_j|<=B k^6`;
3. all variants in `V_j` use one moving/history core `K_j`, and every
   nonanchor core resource belongs to at most `mu` of the `K_j`;
4. outside the core resources, every literal history, cap, provider,
   protected-upper, or topology resource has total load at most `Gk^6` in
   `union_j V_j`;
5. every variant uses at most `A d` nonanchor resources and passes the exact
   cap-surplus, bi-history, whole-component, topology/voltage, and exterior
   return conditions; and
6. its protected bank satisfies (4.1).

Then

\[
                         V=\bigcup_{j\in J}V_j           \tag{5.2}
\]

is a completed subatlas with

\[
 |V|\ge\alpha\beta k^7,qquad
 |\operatorname{supp}_{nonanchor}(v)|\le Ad,qquad
 \max_q\deg_V(q)\le(\mu B+G)k^6.                      \tag{5.3}
\]

#### Proof

The size and support inequalities are immediate.  A core resource occurs in
at most `mu` core fibres, each of size at most `Bk^6`.  All other resources
are controlled by item 4.  The semantic validity of every member is items
5--6. \(\square\)

The intended economy is exact: the original fixed-skeleton product used
seven `Theta(k)` extension choices.  A selector compound uses one
`Theta(k)` degree to move the physical skeleton and retains six
`Theta(k)` degrees inside each selected core.  This is the smallest possible
degree trade by Proposition 5.1.

One prospective physical form is a neutral selector ear `E_j` and its
return around a coprime packet,

\[
                       E_j^{-1}\circ Z\circ E_j,         \tag{5.4}
\]

where all compounds have the same external root/cap/history state but the
intermediate moving cores `K_j` have bounded overlap.  Formula (5.4) is a
specification, not a constructed Boolean packet.  Merely translating `Z`
through the `Z_k` phase action is not enough: all translates are phases of
the same developed quotient packet and do not give independent physical
ticket choices.  Varying the owner `X` in (0.1) likewise changes the private
task rather than supplying the selector required by (5.1).

## 6. Exact remaining gate

The full bounded-load statement is therefore separated as follows.

* **Closed:** central cap/retained resources have the one-degree load
  `O(k^6)` once a moving skeleton is fixed; fixed `O(d)` collar and named-cap
  banks are individually plantable under (4.1).
* **Refuted on the fixed-root raw atlas:** a `Theta(k^7)` fibre with only
  `(7!)^2` moving skeletons has a single moving/history token of load
  `Omega(k^7)`.
* **Live replacement:** construct `Omega(k)` selector-return compounds for
  the same rooted task, each with `Theta(k^6)` completed variants and
  bounded core overlap, and give a balanced provider/history assignment as
  in Theorem 5.2.

This is a physical correlation gate.  Neither the global marginal owner
count (0.1) nor separate abundance of cap providers and history collars can
replace the missing selector.

## 7. Audited inputs

This audit uses the following current files and scopes.

```text
fd0286627e0272908d828e413c63a8f42dad95e109bd98c6489702436b10488c
  MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md
034ea200ee8ec9e1fda177261a3082c9583fcae2ced2f2230d38b42f68c243f3
  MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md
33e97bcdf72b817396523e56f85a077c8649a5a2aabd684bcd1ca8e10b92c8e8
  MATH_THEOREM_HEPTAGON_PROTECTED_HOST_AND_DUPLICATE_CAP_BACKUPS_20260802.md
87cb2be6e37b27e4d04cd0016cbc303fab7fee3ce1cfcb976e7e257ed53dd8d7
  MATH_AUDIT_K_HEPTAGONAL_CAP_CIRCULATION_HOLONOMY_AND_BACKUP_SCOPE_20260802.md
```

The negative result is purely fibrewise and does not use a finite search.
It does not refute a global atlas whose task is allowed to vary `X`, nor a
future Boolean construction which supplies the selector-return family in
Theorem 5.2.  It refutes only the claimed inference from the existing raw
twisted count and local provider theorem to the fixed-root completed-ticket
load bound.
