# Uniform co-instantiated bounded-charge reset spine

**Date:** 2026-08-03  
**Status:** exact implication and quantifier audit.  The implication to
`nu(k) <= B(k) + O(1)` is proved.  The reset-spine existence theorem stated
below is not proved.

## 0. Verdict

Within the current regenerative/common-host architecture, the shortest
honest missing statement is the existence of one compatible infinite odd
spine with uniformly bounded odd and even terminal charges.  It is not
necessary to prove a transition from every admissible parent, zero defect,
one phase-common terminal compiler, or strict contraction.

The implication chain is

```text
one co-instantiated literal transition certificate
  -> complete bounded terminal eviction and terminal repair
  -> terminal/auxiliary phase decoupling
  -> one compatible bounded-charge odd spine with even taps
  -> nu(k) <= B(k) + O(1).
```

All local bank, occurrence, matching, upper, residence, compiler, and
regeneration rows must hold in the same materialized child.  A conjunction of
marginal existential statements is not a transition certificate.

## 1. Exact interfaces

Let `G_m` be a declared family of auxiliary states on `2m+1` coordinates.
Let

\[
 \mathcal P_m^{\rm odd}\subseteq G_m\times G_{m+1},
 \qquad
 \mathcal P_m^{\rm ev}\subseteq G_m\times A_{2m+2}
                                                               \tag{1.1}
\]

be literal odd-successor and even-terminal relations.  Membership is
witnessed by a complete certificate, not merely a tuple of defect counts.
An odd state also has its own odd terminal physicalization.

For a terminal certificate `C`, let

\[
                     \tau(C)=c(C)+R(\mathcal H(C))              \tag{1.2}
\]

be its total terminal charge.  Here `B(k)+c(C)` is the length of its literal
scaffold, \(\mathcal H(C)\) is the complete family of omitted targets after
the final global replay, and \(R(\mathcal H)\) is the minimum length of a
repair word for that family.  Literal listing gives
\(R(\mathcal H)\le |\mathcal H|\).

Terminal compiler eviction is included in (1.2) only after one final word,
cap state, reference matching, and complete damage set have been fixed.  If
`h` hard task cells are installed and the complete damage set meets `d`
cells of the reference matching, then `d+h` old targets are charged before
forming `H(C)`.  Marginal packet damage is not a complete damage set.

## 2. The one missing theorem

### Uniform co-instantiated bounded-charge reset-spine theorem

There exist an absolute integer \(m_0\) and an absolute constant
\(C<\infty\), and entire sequences

\[
 (g_m,a_m,\mathcal C_m^{\rm odd},\mathcal C_m^{\rm ev})_{m\ge m_0},
                                                               \tag{2.1}
\]

such that for every `m >= m_0`,

\[
 \begin{aligned}
 &g_m\in G_m,\\
  &\mathcal C_m^{\rm odd}
       \text{ jointly witnesses }(g_m,g_{m+1})\in\mathcal P_m^{\rm odd}
       \text{ and the odd terminal at }2m+1,\\
  &a_m\in A_{2m+2},\\
  &\mathcal C_m^{\rm ev}
       \text{ witnesses }(g_m,a_m)\in\mathcal P_m^{\rm ev},\\
  &\max\{\tau(\mathcal C_m^{\rm odd}),
           \tau(\mathcal C_m^{\rm ev})\}\le C.
 \end{aligned}                                               \tag{2.2}
\]

The odd certificate exports `g_(m+1)` literally, including every boundary,
provider, residence, history, occurrence, and compiler coordinate declared
by `G_(m+1)`.  Equality of a defect count or reuse of a parent-local
catalogue is not regeneration.

For each certificate, the safe internal quantifier order is schematically

\[
 \begin{split}
 \exists Z\;\exists S\;\exists H_{\rm str}\;
 \exists(\omega_0,\omega_1)&\in
       \Omega_0(Z,S,H_{\rm str})\times_{\mathcal F}
       \Omega_1(Z,S,H_{\rm str})\\
 \exists Q\;\exists M&\subseteq
       \mathcal G_Q(Z,S,H_{\rm str},\omega_0,\omega_1)\\
 \exists\mathcal H\quad &[R(\mathcal H)\le C
   \ \land\ 
   \forall T\notin\mathcal H\ 
      \exists\text{ a literal interval witness for }T\text{ in }Z].
                                                               \tag{2.3}
 \end{split}
\]

`Z` is the one fully materialized child, `S` is the selected structural
family, `H_str` is the common structural host/boundary, the `omega_phi` are
complete phase-local integral occurrence banks, `F` contains only justified
cross-phase equalities, `Q` is the fixed root/common-basis/cap state, and
`M` is the required child-local matching or linkage object.  The phase
tuples may be physically different.  Exact tuple equality is imposed only
when the schema explicitly declares a common occurrence.

Equation (2.3) is schematic but its quantifier order is part of the theorem:
one may not replace it by separate structural, occurrence, supplier, or
compiler witnesses living in different children.

## 3. Implication to the additive bound

### Theorem 3.1

The reset-spine theorem implies

\[
                         \nu(k)\le B(k)+O(1).                   \tag{3.1}
\]

More precisely, for every `k >= 2m_0+1`,

\[
                         \nu(k)\le B(k)+C.                      \tag{3.2}
\]

#### Proof

For `k=2m+1`, use the odd terminal certificate at `g_m`.  Its scaffold has
length `B(k)+c`, and every omitted target belongs to \(\mathcal H\);
appending a repair word of length \(R(\mathcal H)\) gives a universal word
of length `B(k)+tau <= B(k)+C`.
For `k=2m+2`, use `C_m^ev` identically.

The terminal repair word, final compiler matching, and terminal cap state
are not exported to `g_(m+1)`.  Thus the charge is paid once at the requested
dimension and is not added to later word lengths.  Compatibility of the odd
certificates in (2.2) supplies the infinite auxiliary spine.  The finitely
many dimensions below `2m_0+1` are absorbed by enlarging the absolute
constant.  \(\square\)

This is exactly the bounded-cost odd-spine implication.  Bounded compiler
eviction and phase decoupling justify the deliberately weak terminal rows;
zero-defect compilation and a common terminal compiler are unnecessary.

## 4. Quantifier audit

The top-level order is

\[
 \boxed{
 \exists m_0,C\;
 \exists(g_m,a_m,\mathcal C_m^{\rm odd},
                 \mathcal C_m^{\rm ev})_{m\ge m_0}\;
 \forall m\ge m_0.}                                    \tag{4.1}
\]

The following replacements are invalid.

1. `forall m exists C_m`: the charges need not be uniformly bounded.
2. `forall m exists (u_m,v_m)`: the individually good transitions need not
   concatenate into a spine.
3. `and_j exists C_j P_j(C_j)`: owner, chronology, occurrence, residence,
   common-cap, supplier, and compiler witnesses may live in different
   children.
4. `forall phase exists H_phase`: this does not give one structural host.
   A common structural host does not, conversely, require one common
   terminal compiler.
5. `forall role exists occurrence`: phase-local unit capacities and global
   declared flags can make the simultaneous occurrence packing empty.
6. `forall target exists Z_T`: the word must be fixed before its target
   witnesses are chosen.
7. `at most C new casualties per step`: the carried debt may then grow by
   `C` at every step.  Equation (2.2) bounds total terminal charge, while the
   odd export must independently close every carried row.

The stronger left-total form

\[
 \exists C\;\forall m\;\forall g\in\mathcal S_m\;
 \exists g',\mathcal C\quad\mathsf{Reset}_m^C(g,g';\mathcal C) \tag{4.2}
\]

is convenient for induction, but is not minimal.  One selected spine is
enough for an upper bound.

## 5. How the proved exact lemmas meet the missing theorem

The following implications are already exact.

1. **Terminal repair.**  A length-`B(k)+c` scaffold missing exactly `H`
   gives length at most `B(k)+c+R(H)`.
2. **Bounded compiler eviction.**  After the final word and complete damage
   set are fixed, only the matched damaged cells and occupied hard-task cells
   need be charged.
3. **Phase decoupling.**  The terminal plus compiler may differ from the
   auxiliary phase; terminal casualties need not be exported.
4. **Resident collars and protected upper-tail completion.**  These close
   local residence and upper-tail rows under their displayed hypotheses,
   but do not construct the common rooted forest/connector or bound ambient
   damage.
5. **Corrected pull clock.**  The triangular residual vector has a rational
   stationary literal circulation.  This does not give one-copy integral
   owner rounding, a connected Euler chronology, or a pushforward into one
   protected host.
6. **Aligned birail telescoping.**  Literal value counters cancel on a
   genuinely aligned circulation.  Counter cancellation is not an
   occurrence-labelled Hall matching.
7. **Atomization and trapped-menu gammoids.**  After a coherent terminally
   closed bank is selected and replayed in one child, its supplier claims
   have the exact strict-gammoid/min-cut rank.  This theorem does not select
   or materialize the bank.
8. **Loss-normalized contraction.**  For a fixed exposed claim bank,

   \[
      p=q+g-\Delta,
      \qquad
      \Phi'\le\Phi-g+\Delta+c_{\rm ns}.                \tag{5.1}
   \]

   Hence the exact normalized surplus

   \[
        g-\Delta-c_{\rm ns}\ge\rho\Phi-C_0             \tag{5.2}
   \]

   gives `Phi' <= (1-rho)Phi+C_0` on that same child.

Items 4--8 are proof interfaces for constructing the certificates in (2.2),
not additional implication hypotheses once the bounded-charge spine has
been supplied.

## 6. Coordinated proof obligations

The reset-spine theorem should be attacked as one co-instantiation problem,
with four proof obligations whose witnesses must be joined before promotion.

### O1. Integral host and chronology

Push the proved fractional pull-clock/rotor law to one phase-common
structural host with one-copy named owners, a connected or serializable
chronology, and the exact carried boundary.  Fractional stationarity or a
host in each phase separately is insufficient.

### O2. One-child terminally closed bank

Select all source/helper or replacement modules jointly in one child.
Close occurrence, endpoint, address, history, reset, residence, upper,
topology, common-cap, and compiler dependencies.  Mutual support and donor
deletion make the primitive feasibility system nonhereditary; no matroid or
submodularity shortcut is available before atomization.

### O3. Complete service and casualty surplus

On the already fixed child, prove either the exact normalized surplus (5.2)
or a sufficient anchored trapped-menu factorization.  Every remote compiler,
upper, occurrence, and chronology casualty not closed inside the bank belongs
to `c_ns`.  Supplier rank and occurrence feasibility cannot be certified on
different children.

### O4. Literal regeneration and both terminal parities

Prove that the accepted odd child is literally an admissible next state with
fresh child-local catalogues and the same uniform bounds.  Separately supply
the odd terminal and even terminal certificates at each level.  Odd-only
regeneration proves only an odd subsequence.

No obligation may be declared solved from a marginal witness.  The promotion
object is the complete certificate `C_m` in (2.3).

## 7. Why weaker bridges fail

* Local rescue gives `forall obligation exists action`, not one compatible
  action bank.
* Separate phase matchings can have incompatible crossed choices.
* A source/helper pair may be feasible while both singletons are infeasible;
  adding a mode can also delete a needed donor.  Primitive feasibility is
  neither hereditary nor monotone.
* Good states in every dimension need not form a compatible path.
* Pointwise contraction factors below one are insufficient when they tend to
  one; the additive convolution can diverge.
* A bounded shared occurrence or supplier separator can collapse an
  arbitrarily large formal bank to rank one.
* A transported occurrence is not a native child occurrence unless it is
  revalidated in the child-local phase semantics.

Strict affine contraction with dimension-independent constants is a useful
stronger certificate for (2.2).  It is not necessary: a bounded invariant
spine, including the endpoint `rho=1, beta=0` from a bounded seed, already
suffices.

## 8. Scope caveat

The reset-spine theorem is the weakest missing theorem **within the current
regenerative/common-host architecture**.  Across all possible architectures,
a direct per-dimension serial reachability theorem with uniformly bounded
terminal charge would be even shorter, but would essentially bypass the
regenerative interfaces developed here.

No finite-dimensional source cover, local rescue census, fractional
circulation, or parent-specific selector proves (2.1)--(2.3).  This note
therefore establishes no new unconditional bound on `nu(k)`.
