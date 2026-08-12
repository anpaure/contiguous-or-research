# PCPS first clause: exact Rado--erosion factorization

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot existence  
**Status:** exact equivalence after one candidate chronology/support and its
window occurrences are fixed.  The theorem does not construct that outer
chronology and makes no `B+1`, compiler, regeneration, or K17-word claim.

## 0. Outcome

The first missing clause of `PCPS(m,d)` splits exactly into two independent
finite tests once one prospective post-insertion depth chronology has been
chosen.

1. **Boolean source/address closure.**  All source letters have one pointwise largest
   candidate, obtained by intersecting the target sets of every prescribed
   window using that address.  Literal source existence is equivalent to
   explicit pin, nonempty-envelope, and target-coverage containments.
2. **Upper representative closure.**  On an incidence-matching support,
   tail and head injectivity are hereditary.  Selecting one representative
   of every immediate-upper colour while retaining the protected forest is
   exactly Rado's theorem in the contracted rooted graphic matroid.

All non-set boundary/history labels, their global address quotient, and
their accepting automaton state are fixed prospective data, not consequences
of the Boolean inequalities.  Subject to that guard, the two tests share the
chronology but no decision variable: marking a rooted
representative does not change a source letter, and choosing the maximal
source antecedent does not change an incidence occurrence.

For a rooted path support the Rado inequalities collapse to one occurrence
of each upper colour.  A lower-rainbow rank-`m` Johnson owner path plus its
outer rank-`m-1` endpoint ticket gives such a rooted support only after the
endpoint phase is fixed as in (1.4a)--(1.4c) below.  On that phase, uncapped
envelope nonemptiness is automatic when `m>d`; the source lift is then
equivalent to residence of the **full** depth row.  Finally, a fixed literal
split-core pivot fragment requires only its
`2d` boundary-rail containments and at most `2d` exterior coverage rows,
plus named-pin injectivity and the already fixed global address/history
guard.  Thus neither upper-representative selection nor
source-address realization is a remaining Catalan-scale search after the
support chronology is born.

The exact outer host problem left by this theorem is stated in Section 4.

## 1. Fixed prospective data

Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal V={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

and put `W=|mathcal L|=|mathcal V|`, `U=|mathcal U|`, and
`C=W-U=Cat_m`.

Fix the following common data **before** either side of the factorization is
solved.  In particular, `T`, all witness intervals, pins, caps, the global
address quotient, `M_0`, `S`, and `F` may not be changed after the Boolean or
Rado choice is made.

1. A full post-insertion depth word
   \[
                         T=(T_0,\ldots,T_{N-1}).       \tag{1.1}
   \]
   On the one-credit face, `N=W+1`: exactly `W` rank-`m` cells form the
   intended Hamilton owner subsequence and the remaining outer cell is the
   controlled rank-`m-1` endpoint ticket.  The source-address set then has
   `N+d=W+d+1` positions, exactly `B+1` when `B=W+d`.
2. A source-address set `J={0,...,N+d-1}`, lower pins `P_j`, upper caps
   `C_j`, and a family `mathcal H` of prescribed nonempty address sets.  For
   each `H in mathcal H`, a literal target `R_H` is required:
   \[
                            \bigcup_{j\in H}A_j=R_H.    \tag{1.2}
   \]
   The family includes every depth window.  It may additionally include the
   deleted-star crossing windows, selected preword upper occurrences, pivot
   collars, and compiler intervals.  Every occurrence-labelled pin also
   carries its resulting global interval address and any required
   capacity-one distinctness relation.
3. A perfect predecessor matching `M_0:mathcal L -> mathcal V`, and one
   occurrence-labelled incidence matching support `S` outside `M_0`, read
   from the fixed owner phase of (1.1).  For `e=LV in S`, put
   \[
     \lambda(e):L\longrightarrow M_0^{-1}(V),\qquad
     \operatorname {up}(e)=M_0(L)\cup V.              \tag{1.3}
   \]
4. A forced set `F subseteq S` which is a rooted forest, has distinct upper
   colours, contains the complete protected pivot successor path, and
   contains every transition segment declared immovable by the chosen
   witness bank.
5. One globally addressed occurrence quotient and all non-set boundary,
   phase and owner-history labels induced by `T`, already checked for
   consistency and acceptance.  The theorem below preserves this state; it
   neither chooses it nor derives residence from (2.1).

The endpoint aperture is part of the fixed data.  In an unrooted input with
omitted lower root `o` and owner endpoints `s,t`, require

\[
                         o\subset s\quad\hbox{or}\quad o\subset t.    \tag{1.4}
\]

On a rooted input this containment is already encoded by `M_0`.

For later use, spell out the endpoint phase.  Let the lower-rainbow owner
path be `T_0,...,T_(W-1)` and put

\[
                         X_i=T_i\cap T_{i+1}.          \tag{1.4a}
\]

If `o subset T_0`, take

\[
 M_0(o)=T_0,\qquad M_0(X_i)=T_{i+1},\qquad
 S_{\rm path}=\{X_iT_i:0\le i<W-1\}.                 \tag{1.4b}
\]

The rooted arcs are `X_0->o` and `X_i->X_(i-1)` for `i>0`.  If instead
`o subset T_(W-1)`, take

\[
 M_0(X_i)=T_i,\qquad M_0(o)=T_{W-1},\qquad
 S_{\rm path}=\{X_iT_{i+1}:0\le i<W-1\};             \tag{1.4c}
\]

the arcs are `X_i->X_(i+1)` for `i<W-2` and `X_(W-2)->o`.  In either phase
the colour on the `i`th support incidence is exactly
`T_i union T_(i+1)`.  Thus neither an arbitrary perfect `M_0` nor an owner
path with repeated `X_i` automatically supplies the rooted path support.

For each residual upper colour
`R in mathcal R=mathcal U minus up(F)`, define

\[
 E_R=\{e\in S-F:\operatorname {up}(e)=R\},\qquad
 E(X)=\bigcup_{R\in X}E_R.                            \tag{1.5}
\]

Let `M_gr` be the graphic matroid of the rooted occurrence multigraph
`lambda(S)`; opposite directed occurrences are parallel graphic elements.

At a source address put

\[
 \widehat E_j=C_j\cap\bigcap_{H\in\mathcal H:\,j\in H}R_H,          \tag{1.6}
\]

where a row-free intersection contributes the full coordinate universe.

## 2. Exact product theorem

### Theorem 2.1 (protected Rado--erosion factorization)

For the fixed data of Section 1, the following are equivalent.

1. There are nonempty source letters `A_j` and a marked incidence set
   `Q_0` such that
   * `P_j subseteq A_j subseteq C_j` and every equation (1.2) holds;
   * `F subseteq Q_0 subseteq S`;
   * `up:Q_0 -> mathcal U` is a bijection; and
   * `lambda(Q_0)` is a forest.
2. Both of the following families of inequalities hold:

   **Boolean closure**
   \[
   \begin{aligned}
     &P_j\subseteq\widehat E_j,\qquad \widehat E_j\ne\varnothing
         &&(j\in J),\\
     &R_H\subseteq\bigcup_{j\in H}\widehat E_j
         &&(H\in\mathcal H);                           \tag{2.1}
   \end{aligned}
   \]
   and all declared capacity-one named-pin addresses are distinct after the
   fixed global quotient;

   **contracted graphic Rado**
   \[
      r_{M_{\rm gr}/\lambda(F)}\bigl(\lambda(E(X))\bigr)\ge |X|
          \qquad(X\subseteq\mathcal R).                \tag{2.2}
   \]

When (2.1) holds, `A_j=widehat E_j` is the unique pointwise maximum source
word.  When (2.2) holds, any independent transversal supplied by Rado,
together with `F`, is a valid `Q_0`.  The two choices can be made
independently.

#### Proof

Every feasible source letter at address `j` lies in its cap and in every
target union whose address set contains `j`, so it lies in `widehat E_j`.
Pins and nonempty letters give the first line of (2.1), while each target
union gives the second.  Named-address distinctness is independent of the
set value placed at an address and is therefore a separate literal quotient
test.  Conversely, taking `A_j=widehat E_j` cannot add an unwanted
coordinate to any target row, and the coverage inclusion in (2.1) prevents
a missing coordinate.  This proves exact source closure and maximality.

Because `S` is an incidence matching, every subset has distinct rooted
tails and heads.  After contracting the forced forest `lambda(F)`, choosing
one occurrence from every residual colour family while retaining
acyclicity is precisely an independent transversal in `M_gr/lambda(F)`.
Rado's theorem is exactly (2.2).

Finally, selecting `Q_0` only marks occurrences already present in the fixed
chronology, while replacing a source antecedent by its maximal member changes
no prescribed target row or incidence occurrence.  Hence the two
constructions coexist.  \(\square\)

The last paragraph is a genuine hypothesis boundary: if choosing a residual
representative activates a new occurrence-specific cap, pin, history, or
witness row, that row was not fixed in Section 1 and the product statement
does not apply.  Such alternatives must first be expanded into the fixed
support state (or solved jointly).

Writing `kappa_F(X)` for the cycle nullity of `F union E(X)`, the graphic
rank identity gives the completely explicit equivalent form

\[
             |E(X)|-\kappa_F(X)\ge |X|.                \tag{2.3}
\]

Its exact upper-representative deficiency is

\[
 \delta_F(S)=\max_{X\subseteq\mathcal R}
       \bigl(|X|-|E(X)|+\kappa_F(X)\bigr).              \tag{2.4}
\]

Thus the first protected host exists for the fixed support exactly when
(2.1) holds and `delta_F(S)=0`.

### Corollary 2.2 (path and single-cycle supports)

If `lambda(S)` is a rooted forest or path, (2.2) is equivalent to

\[
                              E_R\ne\varnothing
                  \qquad(R\in\mathcal R).              \tag{2.5}
\]

The same conclusion holds when `lambda(S)` is one spanning rooted cycle
and `F` is a proper subforest: the Catalan excess `W-U=C` pays the only
possible completed-cycle rank loss.

Consequently, on an already replayed rooted Hamilton path or cycle, an
upper-exact protected Catalan forest costs no further multi-resource
selection theorem: every upper colour merely needs one occurrence.

#### Proof

On a rooted forest, `F union E(X)` is independent, so its contracted rank is
`|E(X)|`.  Since the residual colour classes are disjoint, their individual
nonemptiness is equivalent to `|E(X)|>=|X|` for every `X`.

On one spanning cycle the rank falls by one only if `F union E(X)` contains
the entire cycle.  Then `|E(X)|=W-|F|`, while
`|X|<=U-|F|`; hence `|E(X)|-1>=|X|` because `W-U=C>=1`.
Otherwise there is no cycle-rank loss.  \(\square\)

## 3. Literal Johnson-host corollaries

### Corollary 3.1 (uncapped resident host)

Assume the full row (1.1) consists of a rank-`m` Johnson Hamilton owner path
`T_0,...,T_(W-1)` whose `W-1` consecutive intersections `X_i` are pairwise
distinct, followed by the unique omitted rank-`m-1` root `o` as its outer
boundary ticket, with `o subset T_(W-1)`.  Use the terminal phase (1.4c):
`M_0(X_i)=T_i`, `M_0(o)=T_(W-1)`, and
`S_path={X_iT_(i+1)}`.  Assume `m>d`, the protected pivot successor path is
contained in this `S_path` with its certified orientation, the full row is
depth-`d` resident, and every one of the `U` immediate-upper colours occurs
among its adjacent unions.

Then the source has `W+d+1=B+1` letters, and:

1. the uncapped full row has a canonical pointwise-maximal nonempty source
   antecedent;
2. the owner-path support contains an upper-exact rooted Catalan forest
   `Q_0` containing the pivot successor path; and
3. every upper target already witnessed by a consecutive interval of the
   full depth row is witnessed by the corresponding source interval.

#### Proof

Any `d+1` consecutive rank-`m` Johnson owners have intersection rank at
least `m-d`.  A window containing `o` starts with its `m-1` elements, loses
nothing at the containment step, and then loses at most `d-1` elements, so
has the same lower bound.  Envelope nonemptiness is automatic; full-row
residence is therefore exactly the uncapped source-lift condition.

Equation (1.4c) gives the perfect phase `M_0`; the successor incidences are
an incidence matching whose rooted support is one path and whose colours
are precisely the adjacent unions.  Corollary 2.2 selects
`Q_0`, forcing the protected occurrences for their distinct colours.  Finally
`union_(i=p)^q T_i=union_(j=p)^(q+d)A_j` transports every displayed upper
witness.  \(\square\)

### Corollary 3.2 (bounded literal pivot-extension rows)

Suppose a fixed literal source fragment `B` already factors an `n`-cell
pivot depth block inside the uncapped resident host of Corollary 3.1, with
`n>=d`, and all its internal depth equations have been replayed.  Embedding
`B` into the canonical antecedent is then equivalent to the remaining
boundary conditions:

* containment of the first and last `d` source letters of `B` in their
  global maximal envelopes; and
* coverage of the at most `d` exterior depth cells on each side whose
  windows meet `B`.

Thus the split-core pivot (`n=3d+1`, source length `4d+1`) has at most `2d`
rail-containment and `2d` exterior-coverage rows.  External named-pin
injectivity remains a separate literal check.  There is no Catalan-scale
source-address gate for planting this fixed collar after the chronology is
chosen, but the fixed global quotient and boundary/history acceptance still
have to pass.

## 4. The exact remaining host lemma

Theorem 2.1 removes both the source-letter variables and the upper-
representative variables.  The smallest remaining outer assertion is:

> **Protected chronology-support lemma `PCS(m,d)`.**  In the literal-pivot
> range `m>=3d+1`, construct one full
> post-insertion depth chronology and its rooted incidence-matching support
> such that:
> 1. its `W` owner cells form a lower-rainbow Johnson Hamilton path with the
>    corrected terminal endpoint ticket and phase (1.4c), and contain the
>    literal pivot successor collar;
> 2. every colour in the full immediate-upper shore has an eligible
>    rooted incidence occurrence on that support, including every
>    exceptional boundary/`D` colour of rank `m+1`; any additional
>    boundary/opening target outside that immediate-upper shore has a
>    prescribed literal window occurrence in `mathcal H`;
> 3. the full depth row is resident and its fixed pivot rails pass the
>    `4d` bounded extension rows of Corollary 3.2;
> 4. every required post-insertion strictly higher upper target has a
>    selected depth-interval witness; and
> 5. the old crossing sets and one pre-insertion witness interval per target
>    can be chosen so that the Boolean closure inequalities (2.1) pass after
>    deletion of the marked star.

An `mathcal H` row certifies an interval-OR occurrence; it cannot replace a
missing rooted incidence occurrence in the `Q_0` colour shore.

`PCS(m,d)` implies the rooted upper-exact protected host and its complete
global source/address/history replay.  It is strictly smaller than
`PCPS(m,d)`: the terminal common-cap/lower-compiler assignment and
regeneration of the next prepared cut remain separate.  Conversely, every
`PCPS` certificate in the corrected prepared-scaffold formulation restricts
to `PCS`.

The first three rows of `PCS` are the clean support-first target.  Rows 4--5
are the all-width/preword chronology gate; post-insertion upper completeness
alone does not imply them.

## 5. K17 calibration, with fail-closed scope

The independently certified three-hole checkpoint is

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
    weighted3.independent.model
SHA-256 b2b5d2c6dfa14552b4b80c2c0d69920096dc9e4b9bbc3f5c35a3360df90a416c
```

It has connected lollipop topology and covers `19,409/19,412` necessary
non-`D` rank-10 tasks.  The missing masks are

\[
              32058,\qquad 103907,\qquad109870.        \tag{5.1}
\]

The endpoint projection is compatible with the corrected aperture:
`M=0x17f subset B=0x1ff`.  This is useful evidence for Row 1 of `PCS`, but
the augmented factor is not yet the replay-bound support of Theorem 2.1;
one must choose its predecessor phase, delete the correct `D`-tail, and bind
the result to one literal source chronology.

The restricted `19,412`-task score is also not the full immediate-upper
task shore.  Literal replay has rank-10 holes

\[
                             25=3+22,                  \tag{5.2}
\]

where the stable extra `22` are boundary/`D` colours of the same rank-ten
shore.  Because `Q_0` must be bijective onto the **full** immediate-upper
shore, all 22 require eligible rooted incidences in `S`; prescribing only
their interval windows in `mathcal H` would preserve deck coverage but would
not supply `Q_0`.  They cannot be hidden in scalar Catalan slack.
The same replay has rank-11/12/13 holes `1534/291/7` and short-run debt
`5578`, so Rows 3--5 fail.

The one-hole checkpoint `transport3_2.best.model` is now independently
authenticated by
`MATH_AUDIT_K17_H1_STATIC_C6_C8_CHAIN_AND_ONEHOLE_MODEL_20260802.md` and
`scratch/k17_h1_q1_onehole_transport3_2_independent_20260802.audit.json`.
Its model SHA is
`be00a9d0b2470cd334a0b51476185c2ef61c99d28ce61b12f2ff32c26bcac213`,
and its independent audit JSON SHA is
`b4401058201ed6cb40c0f3a16640d737da8ddd684ecc980f2e475ea6e2957f95`.
It has one remaining necessary non-`D` task, mask `32058`.  Its literal
rank-10/11/12/13 holes are nevertheless `23/1532/286/7` and its short-run
debt is `5584`; in particular, the other 22 rank-ten colours still fail the
full Row 2 support shore.

The successor `q1zero.independent.model` is also independently authenticated
on the restricted `19,412` non-`D` shore.  Its literal orientation still has
rank-10/11/12/13 holes `22/1533/286/7` and `5586` short positive runs.
Thus neither authenticated checkpoint proves a complete Row 2 incidence
support, residence, source replay, or any later `PCS` row.  Both are
augmented lollipop factors, not yet the `W-1`-incidence rooted path support
required by Corollary 3.1.

## 6. Scope

Unconditional in this note:

* the product equivalence (2.1)--(2.2) for fixed prospective data;
* the exact graphic-Rado deficiency (2.4);
* automatic upper selection on path and single-cycle supports;
* automatic uncapped envelope nonemptiness for the intended Johnson host;
* the bounded `4d` literal pivot-extension row count; and
* the exact implication `PCS ->` rooted upper-exact source-replayed host.

Open:

* `PCS(m,d)` for all parameters;
* choice of the old crossing sets and preword upper occurrence intervals;
* the terminal common-cap/lower compiler;
* regeneration;
* completion and source binding of the K17 **full** immediate-upper shore;
* any improvement of the K17 upper bound.
