# K16 upper-12874 delete-plus-two-substitution target-closure MITM

Date: 2026-07-31  
Lane: D  
Status: exact reduction/theorem; no new census result is claimed here

## 1. Frozen source and the precise remaining branch

Let

```text
U = answers/k16_upper12874.word
|U| = 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

The exact all-deletion/all-one-substitution theorem proves that no universal
length-12873 word is obtained from `U` by deleting one cell and changing at
most one surviving cell.  The exact global all-joint theorem separately
closes every two-change candidate in which every deletion hole has a final
witness containing both changed sites.  Its scope is a strict branch, not a
global radius-two theorem.

This note gives a proof-complete formulation of the complementary branch:
at least one changed site, applied by itself to the deletion word, supplies at
least one original deletion hole.  It is designed for the seven repository
"low-hole" deletion basins (exactly the basins with at most three holes), but
the theorem is valid for every deletion.

The seven frozen basins are

| deleted source index | exact holes | basin SHA-256 |
|---:|---|---|
| 0 | `0x4879,0x6879` | `d7464163340dea186ecc97ef395ced92c08642972f54e22c3584e3ae33c453dc` |
| 1 | `0x2c6d` | `a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649` |
| 3 | `0x146d,0x546d` | `2748072c5eb786523a735895119452855cfeca9eb41799989f9f531caafb75eb` |
| 6389 | `0x4679,0x6a61,0x6b61` | `ca03499c5b657714472b743bad9805a9ae18ef66f51c27e7ddbf94a13da97f56` |
| 6441 | `0x946d,0xa86d,0xd46d` | `387beaada1065208f2a7c49d4e1ed0132044c10f05b34d692cd652f9c615e79c` |
| 12871 | `0x8c67,0x8ce7,0xbcef` | `65b8ef432b1a122c24eac0e9a0e141df30236f5755bd67bd1d8f01632d4b38fc` |
| 12873 | `0xce61,0xce63` | `f59a5c3cf55d77352903e2db10157586e17d882da286753ab11b10652cacd579` |

The complete deletion histogram also gives 191 basins with at most four
holes and 1122 with at most five holes.  A production result must therefore
say explicitly whether its deletion set is `D3` (7), `D4` (191), `D5`
(1122), or all 12874 deletions.  The unqualified repository term
"low-hole deletion basins" refers to `D3` in
`scratch/ad_k16_upper12874_lowhole_delete_sub1_20260730/audit.json`.

## 2. Indexing and literal quantifiers

Fix a zero-based source deletion index

\[
 d\in\{0,\ldots,12873\}.
\]

The deletion word `W=W^d` has length `n=12873` and post-deletion indices
`0,...,n-1`.  Its source-index map is

\[
 \iota_d(i)=\begin{cases}i,&i<d,\\ i+1,&i\ge d.\end{cases}
\]

The two substitution sites are **post-deletion** indices `p,q`, with
`0 <= p < q < n`.  The final word is

\[
 V_i=\begin{cases}
 x,&i=p,\\ y,&i=q,\\ U_{\iota_d(i)},&i\notin\{p,q\},
 \end{cases}
 \qquad x,y\in\{1,\ldots,65535\}.                 \tag{2.1}
\]

Thus the deleted cell is never itself substituted.  Reports must retain both
the post-deletion pair `(p,q)` and the surviving source pair
`(iota_d(p),iota_d(q))`; confusing these conventions shifts every site at or
after `d`.

Equation (2.1) initially allows a replacement value to equal its incumbent.
The authenticated deletion and delete-plus-one-substitution no-gos imply that
any universal member of (2.1) necessarily has

\[
 x\ne W_p,\qquad y\ne W_q.                              \tag{2.2}
\]

Consequently a production search may enforce (2.2), but only while pinning
the hashes of those prior theorems.  Equal new values `x=y` are allowed.  The
two sites, not their values, must be distinct.  Two changes of the same site
collapse to the already closed one-substitution case.

Only the 65535 nonzero masks are targets, and cells are required to be
nonzero.

## 3. Exact three-class identity for a fixed support

For a word `Z`, let `c_Z(t)` be the number of nonempty intervals whose OR is
the target `t`.  Fix `p<q` in `W`.  Removing the two sites splits the word into
three fixed runs.  Every affected interval lies in exactly one of

1. intervals containing `p` but not `q`;
2. intervals containing `q` but not `p`;
3. intervals containing both `p` and `q`.

Let `A_{p,q}(t)` count old witnesses avoiding both sites.  Let
`P_{p,q}(x;t)`, `Q_{p,q}(y;t)`, and `B_{p,q}(x,y;t)` count new witnesses in
the three classes.  Then, with no independence assumption,

\[
 c_V(t)=A_{p,q}(t)+P_{p,q}(x;t)+Q_{p,q}(y;t)
                         +B_{p,q}(x,y;t).                \tag{3.1}
\]

The both-site term depends on `x OR y`.  It is not the sum of two single-site
deltas.  Formula (3.1) is the audit identity against which any proposed
pairwise MITM must be checked.

There is a compact exact fixed-support encoding.  For each target `t`, form
the dominance-minimal deficit antichains

\[
 \mathcal D_P(t),\quad\mathcal D_Q(t),\quad\mathcal D_B(t).\tag{3.2}
\]

For example, a `p`-only interval has a fixed outside OR `s`.  It realizes `t`
with value `x` exactly when

\[
 s\subseteq t,\qquad t\setminus s\subseteq x\subseteq t. \tag{3.3}
\]

Delete every deficit `t\s` that strictly contains another attainable
deficit.  The remaining deficits are `D_P(t)`.  The `q`-only antichain is
identical.  For a both-site interval, `s` includes the entire fixed middle
run, and

\[
 s\subseteq t,qquad t\setminus s\subseteq x\mathbin\vee y
                     \subseteq t.                         \tag{3.4}
\]

Thus, for the private target set

\[
 \mathcal P_{p,q}=\{t:A_{p,q}(t)=0\},                    \tag{3.5}
\]

the pair `(x,y)` is feasible iff every `t in P_{p,q}` satisfies at least one
of

\[
\begin{array}{ll}
x\subseteq t\text{ and }D\subseteq x
  &\text{for some }D\in\mathcal D_P(t),\\
y\subseteq t\text{ and }D\subseteq y
  &\text{for some }D\in\mathcal D_Q(t),\\
x\vee y\subseteq t\text{ and }D\subseteq x\vee y
  &\text{for some }D\in\mathcal D_B(t).
\end{array}                                                \tag{3.6}
\]

This is an exact two-variable target-closure CSP.  It is a useful independent
cross-audit, but the sequential form below is smaller for the complete
provider-first branch.

## 4. Exact dichotomy and the partial-provider bank

Let `H_d` be the holes of `W^d`.  Every final witness of a hole meets at least
one changed site, since an interval avoiding both is unchanged and the target
was absent in `W^d`.

### Lemma 4.1 (provider/joint dichotomy)

Every universal two-change word belongs to at least one of:

1. **provider-first:** one changed site, applied alone to `W^d`, supplies at
   least one member of `H_d`;
2. **all-joint:** every `h in H_d` has a final witness containing both changed
   sites.

Indeed, if a final hole witness contains exactly one changed site, applying
that edit alone leaves the witness unchanged and supplies the hole.  If no
such witness exists, every final hole witness contains both sites.  QED.

The existing global all-joint theorem closes branch 2 for all 12874
deletions.  It remains to enumerate **partial** providers, not merely edits
which supply all holes.

For a position `p`, take the distinct ORs of suffixes ending at `p-1` and
prefixes starting at `p+1`, including the empty OR zero, and join them by OR.
For `h in H_d`, retain joined contexts `s subseteq h` and form

\[
 \mathcal D_{p,h}=\min_{\subseteq}{h\setminus s:s\text{ is retained}\}.
                                                               \tag{4.1}
\]

Then the complete literal provider domain at `p` is

\[
 \mathcal X_p=\bigcup_{h\in H_d}
  \{x:0<x\subseteq h,\ D\subseteq x
             \text{ for some }D\in\mathcal D_{p,h}\}.       \tag{4.2}
\]

Equation (3.3) proves both directions of (4.2).  Values generated through
several holes are deduplicated before replay, and the no-op `x=W_p` is
removed using (2.2).

This is the crucial completeness correction to a full-provider-only bank.
A first edit may supply only one of two or three original holes and eject
several old targets; the second edit is allowed to repair all of them jointly.

## 5. The target-core sweep after the first edit

Fix a genuine first provider `P=(p,x)` and materialize the actual intermediate
word

\[
 Z=W^d[p\leftarrow x].                                    \tag{5.1}
\]

For a target `t` represented in `Z`, define

\[
 L_Z(t)=\max\{a:\operatorname{OR}(Z[a:b])=t\},\qquad
 R_Z(t)=\min\{b:\operatorname{OR}(Z[a:b])=t\}.             \tag{5.2}
\]

The intersection of all `t`-witness intervals is exactly

\[
 K_Z(t)=
 \begin{cases}[L_Z(t),R_Z(t)],&L_Z(t)\le R_Z(t),\\
 \varnothing,&L_Z(t)>R_Z(t).
 \end{cases}                                               \tag{5.3}
\]

For an absent target put `K_Z(t)=[0,n-1]`.  Therefore the exact set whose all
current witnesses cross a prospective second site `q` is

\[
 \mathcal R_Z(q)=\{t:q\in K_Z(t)\}.                        \tag{5.4}
\]

This includes every intermediate hole at every site.  Present targets enter
at `L_Z(t)` and leave after `R_Z(t)`, giving a linear event sweep in `q`.

For each cut, store the distinct suffix-OR and prefix-OR chains, including
zero.  Each chain has at most 17 entries.  The exact through-`q` label set
after putting value `y` at `q` is the meet-in-the-middle join

\[
 \Gamma^Z_q(y)=
 \{a\vee y\vee b:a\in\operatorname{SuffixOR}(Z[0:q]),
                    b\in\operatorname{PrefixOR}(Z[q+1:n])\}.
                                                               \tag{5.5}
\]

There are at most `17*17=289` raw joins.  Because (5.5) is built in the
**materialized first-edited word**, the chain on the side containing `p`
contains `x`.  Consequently all intervals containing both edits, including
the nonadditive `x OR y` cross term in (3.1), are present automatically.

### Theorem 5.1 (maximal second-value theorem)

Put

\[
 J_Z(q)=\bigcap_{t\in\mathcal R_Z(q)}t.                    \tag{5.6}
\]

If `R_Z(q)` is nonempty, a nonzero second value `y` gives a universal final
word iff

\[
 y\subseteq J_Z(q),\qquad
 \mathcal R_Z(q)\subseteq\Gamma^Z_q(y).                   \tag{5.7}
\]

Moreover

\[
 \exists y\text{ satisfying (5.7)}
 \quad\Longleftrightarrow\quad
 J_Z(q)>0\text{ and }
 \mathcal R_Z(q)\subseteq\Gamma^Z_q(J_Z(q)).              \tag{5.8}
\]

Proof.  A demanded target has no avoiding witness, so its new witness contains
`q`; hence `y subseteq t` for every demanded `t`, proving `y subseteq J`.
If a context `s` has `s OR y=t`, then

\[
 y\subseteq J\subseteq t\quad\Longrightarrow\quad s\vee J=t.
\]

Thus every witness supplied by `y` remains a witness after replacing `y` by
`J`.  The converse is immediate.  Targets outside `R_Z(q)` retain an avoiding
witness.  QED.

This theorem removes the `65535`-value second loop exactly.

### Genuine-change corner case

The feasible values in `2^{J_Z(q)}` form an upset.  If the maximal value `J`
differs from the incumbent `Z_q`, testing `J` decides the genuine second edit.
If `J=Z_q`, a different nonzero feasible value exists iff at least one coatom

\[
 J\setminus\{b\},\qquad b\in J,                            \tag{5.9}
\]

is nonzero and passes (5.7).  Indeed every proper feasible submask lies below
one such coatom.  Hence at most 16 additional tests are needed; silently
discarding `J=Z_q` would be incomplete.  If `R_Z(q)` is empty, `Z` is already
universal and every value retains an avoiding witness; this branch is ruled
out here by the frozen one-substitution no-go but should remain a fail-closed
assertion in code.

## 6. Canonical enumeration and unordered-pair deduplication

A final word is determined by the deletion `d` and the unordered set of
attached edit records

\[
 \{(p,x),(q,y)\}.                                          \tag{6.1}
\]

Canonicalize physical support by `p<q`; do **not** sort `x,y`, since each
value is attached to its site.  To remove duplicate provider-first orderings:

1. test independently in `W^d` whether `(p,x)` supplies any original hole;
2. do the same for `(q,y)`;
3. if both are providers, choose the smaller post-deletion site as the first
   provider; if exactly one is a provider, choose it; if neither is a
   provider, the row belongs to the already closed joint-only complement.

Distinct-site substitutions commute, so this orientation loses no final
word.  A simpler engine may enumerate both provider orders, but then its exact
counts must distinguish ordered traces from deduplicated final words.

## 7. Proof-complete production algorithm

For each declared deletion set `D3`, `D4`, `D5`, or all deletions:

1. Materialize `W^d` using the map `iota_d` and independently replay its exact
   hole set.
2. Build the cut suffix/prefix OR chains.
3. Generate and deduplicate every partial provider `(p,x)` by (4.1)--(4.2).
4. Materialize `Z=W^d[p<-x]`; build exact coverage, `L_Z`, `R_Z`, and the
   event lists for (5.4).
5. Sweep all `q!=p`.  Form `J_Z(q)` and test (5.8), or the coatoms (5.9) when
   required.
6. Apply the canonical provider ordering of Section 6.
7. For every positive, materialize the literal length-12873 word and perform
   two independent full replays over targets `1,...,65535` (ending-state and
   start-by-start).  Accept only `65535/65535` agreement.

The exact inner work per first provider is linear in `n` times a small
`17*17` OR join, plus the target-core event incidences.  No pair of edits is
evaluated by adding independent loss/gain ledgers.

An exact signature cache is permitted.  Two first-provider/site pairs may be
identified only when both their demanded-target set and their literal
suffix/prefix context banks agree:

\[
 \Sigma(P,q)=
 \bigl(\mathcal R_{Z_P}(q),
       \operatorname{SuffixOR}_{Z_P}(q),
       \operatorname{PrefixOR}_{Z_P}(q)\bigr).             \tag{7.1}
\]

Equal hole sets, equal intersections, or equal marginal deltas alone are not
sound quotient keys.

The first-edit influence can also be stopped exactly once the unchanged
outward run has OR `0xffff`: all longer intervals through the edited site then
have full OR under both values, while intervals not reaching it are baseline
intervals.  This finite-halo cache is an optimization, not a change of
quantifiers.

## 8. Independent audit contract

A negative result is theorem-grade only if the audit verifies:

* source SHA and the declared deletion ledger (`D3`, `D4`, `D5`, or all);
* post-delete/source index maps for every row;
* exact provider domains (4.2), including partial providers;
* genuine-change exclusions justified by the frozen radius-one no-go;
* the provider-order deduplication identities;
* literal first-edited directional chains and target cores on stratified rows;
* maximal-value equivalence (5.8), including all `J=incumbent` coatom cases;
* exact candidate counts and terminal statuses;
* independent full replay of every positive.

Timeout, address-space failure, incomplete shards, or a missing deletion row
is `UNKNOWN`, never `NO_PASS`.

## 9. Relation to prior exact results

The relevant frozen artifacts are:

```text
MATH_AUDIT_K16_UPPER12874_DELETE_PLUS_ONE_SUBSTITUTION_NOGO_20260730.md
  SHA-256 be711aa7826f0403403bf38dae059504a73c5d9f0e1dd0607d6d1758122c6705

MATH_THEOREM_K16_UPPER12874_DELETE_TWO_SUB_ALLJOINT_GLOBAL_NOGO_20260730.md
  SHA-256 a7d6b7e662125510eb51595bc0b101baa26d4599553550b4d3d1a80e157f7239

scratch/ad_k16_upper12874_lowhole_delete_sub1_20260730/audit.json
  SHA-256 5a4f47b1a431241e26b9dfbe8e19af69a6e52d136892c670d131fb45d94740e5

scratch/k16_upper12874_delete_sub1_all12874_20260730/nonzero_common.tsv
  SHA-256 d9b0f51d53f76ee2dcb85cbb0129c1db44225ba9055b87d4a10c847a270969d2
```

The earlier delete-`p1` projected demand-two provider theorem supplies the
same maximal-intersection idea in a different projected/multiplicity problem;
it is not by itself a full 16-bit all-deletion radius-two theorem.  The present
formulation uses literal 16-bit interval coverage and all 65535 targets.

Combining a completed provider-first `NO_PASS` on a declared deletion set with
the existing global all-joint no-go gives an exact delete-plus-two-substitution
no-go on precisely that deletion set.  It does not exclude reordering, three
or more substitutions, a different parent, or an unrelated length-12873 word.
