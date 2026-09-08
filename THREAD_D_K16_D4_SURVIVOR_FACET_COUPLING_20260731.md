# K16 D4 survivor-facet coupling and its deletion-dependent obstruction

Date: 2026-07-31  
Lane: D  
Status: exact structural theorem; no new computational claim

## 1. Setting

Let

```text
U = answers/k16_upper12874.word,
|U| = 12874,
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

For a word `Z`, write `H(Z)` for the nonzero Boolean masks which are not the
OR of a nonempty consecutive interval of `Z`.  If `H(Z)` is nonempty, put

\[
        J(Z)=\bigcap_{t\in H(Z)}t.
\]

For a coordinate bit `b`, let

\[
        F_b=\{t\ne0:b\notin t\}
\]

be the open coordinate facet.  For a nonzero mask `y`, let

\[
        \uparrow y=\{t:y\subseteq t\}
\]

be its principal Boolean filter.

The exact D4 theorem closes the following fixed-parent neighborhood.  Let

\[
 D_{\le4}=\{d:|H(U\setminus U_d)|\le4\}.
\]

The authenticated deletion ledger has `|D_{<=4}|=191`; it consists of the
seven rows

```text
D3 = {0,1,3,6389,6441,12871,12873}
```

with at most three holes and the 184 rows `E4` with exactly four holes.  The
machine-readable exact membership list is

```text
scratch/k16_upper12874_delete_basins_le4_20260730.tsv
SHA-256 62148666bdbe577c7184112e3f6cc8b6f2c8c856c8113fbbff2a3626fbfcbb01.
```

For every `d in D_{<=4}`, deleting `U_d` and replacing at most two distinct
surviving cells by arbitrary nonzero masks does not produce a universal
length-12873 word.  This paragraph only restates the composed D3+D4 theorem;
the new content below is its deletion-independent structural reduction.

## 2. The deletion-independent coupling

> **Theorem 2.1 (principal-filter/facet survivor theorem).**  Let `W` be any
> word and let
>
> \[
>       Z=W[p\leftarrow x],\qquad
>       V=Z[q\leftarrow y],\qquad p\ne q,\qquad y\ne0.
> \]
>
> Assume `V` is universal and `Z` is not universal.  Then
>
> \[
>       0<y\subseteq J(Z),                              \tag{2.1}
> \]
>
> and hence
>
> \[
>       H(Z)\subseteq\uparrow y.                       \tag{2.2}
> \]
>
> In particular, for every `b in y`, the intermediate word `Z` covers the
> entire facet `F_b`.

**Proof.**  Fix `t in H(Z)`.  The final word must acquire a witness for `t`.
Every interval avoiding `q` is unchanged from `Z`, so every new witness of
`t` contains `q`.  Its OR contains the new cell `y`, whence `y subseteq t`.
This holds for every intermediate hole, proving (2.1)--(2.2).  If `b in y`,
no member of `F_b` can contain `y`; therefore no member of `F_b` is an
intermediate hole.  QED.

The converse set identity is also exact:

\[
       J(Z)\ne0
       \quad\Longleftrightarrow\quad
       Z\text{ covers }F_b\text{ for some }b.           \tag{2.3}
\]

Indeed a bit belongs to `J(Z)` exactly when it belongs to every hole.  Thus
the survivor-bit index is not merely a property of the small D3/D4 hole
families: it says that every possible provider-first completion passes
through a one-edit intermediate word which is complete on a full
15-dimensional coordinate facet.  More strongly, the support of the actual
second value gives simultaneous completeness on every facet `F_b`, `b in y`,
and all possible intermediate holes lie in the principal filter
`{t : y subseteq t}`.

For the frozen parent, the authenticated delete-plus-one-substitution no-go
ensures that `Z` is not universal, so the hypothesis excluded in Theorem 2.1
never hides a solution.

## 3. A segmented 15-dimensional normal form

For fixed `b`, split `Z` at every cell containing `b`, and let
`B_1,...,B_s` be the resulting maximal consecutive blocks of cells omitting
`b` (empty blocks are discarded).  Let `Lang(B_i)` be the set of nonzero ORs
of consecutive intervals of `B_i`.

> **Corollary 3.1 (facet block decomposition).**
>
> \[
>       Z\text{ covers }F_b
>       \quad\Longleftrightarrow\quad
>       \bigcup_{i=1}^s Lang(B_i)=F_b.                  \tag{3.1}
> \]

**Proof.**  An interval whose OR omits `b` contains no cell carrying `b`, so
it is wholly contained in one `B_i`.  Conversely every interval in a `B_i`
has OR omitting `b`.  QED.

This is the strongest deletion-independent coupling supplied by the
survivor-bit argument.  It turns the first stage into a segmented
15-coordinate universal-cover condition, independent of how the
intermediate word was produced.  It is potentially useful as a global
separator because there are only 16 facet labels, and a proposed second mask
`y` imposes several such facet conditions simultaneously.

It does **not** imply that one block `B_i` is itself universal, and it gives
no component-count bound.  Treating (3.1) as a single-block condition would
be an invalid strengthening.  There is, however, an exact length consequence:
concatenating the blocks `B_i` retains every internal witness.  The
concatenated word is an ordinary 15-coordinate universal word.  Consequently

\[
       \#\{i:b\notin Z_i\}\ \ge\ \nu(15)=6438.          \tag{3.2}
\]

Equivalently, a survivor bit occurs in at most
`12873-6438=6435` cells of a length-12873 intermediate word.

The full principal-filter statement gives a hierarchy stronger than (3.2).
Put `S=supp(y)`.  For every nonempty `A subseteq S`, split `Z` at cells
meeting `A`, concatenate the remaining maximal blocks, and write

\[
       N_A(Z)=\#\{i:Z_i\cap A=\varnothing\}.
\]

Every target supported on the other `16-|A|` coordinates fails to contain
`y`, hence is covered in `Z`.  The concatenated blocks therefore form a
universal word on those coordinates and

\[
       N_A(Z)\ \ge\ \nu(16-|A|).                       \tag{3.3}
\]

Summing (3.3) over the `a`-subsets of `S` gives the deletion-independent
moment inequalities

\[
 \sum_i {\,|S\setminus Z_i|\,\choose a}
 \ \ge\
 {|S|\choose a}\nu(16-a),
 \qquad 1\le a\le |S|.                                 \tag{3.4}
\]

Equations (3.3)--(3.4) are the part of the survivor index most directly
compatible with a global incidence/waste ledger.  They are necessary, not
sufficient: they forget the order and the through-second-site witness
geometry.

## 4. Exact deletion-dependent obstruction

The face counts have an exact fixed-parent transport law.  If `s` is the
surviving source index edited first and `Z=(U minus U_d)[s <- x]`, then for
every coordinate set `A`

\[
 N_A(Z)=N_A(U)
 -{\bf1}[U_d\cap A=\varnothing]
 -{\bf1}[U_s\cap A=\varnothing]
 +{\bf1}[x\cap A=\varnothing].                         \tag{4.1}
\]

Combining (4.1) with (3.3) gives an exact, inexpensive necessary cut for a
chosen survivor support.  Its dependence on `d` and `s` is explicit.  It is
still only a marginal cut: it does not certify that the required masks occur
as interval ORs.

The facet label does not determine which first edits are possible.  Fix a
deletion `d`, its deletion word `W^d`, a first site `p`, and a bit `b`.  Let

* `H_d=H(W^d)`;
* `V_{d,p}` be the covered targets all of whose `W^d` witnesses contain `p`;
* `C^d_t(p)` be the OR of the maximal `t`-compatible suffix immediately left
  of `p` and maximal `t`-compatible prefix immediately right of `p`.

Define

\[
\begin{split}
 L_{d,p,b}&=\bigvee_{\substack{t\in H_d\cup V_{d,p}\\b\notin t}}
                 \bigl(t\setminus C^d_t(p)\bigr),\\
 R_{d,p,b}&=\bigcap_{\substack{t\in H_d\cup V_{d,p}\\b\notin t}}t.
                                                               \tag{4.2}
\end{split}
\]

With the empty-family conventions `L=0`, `R=0xffff`, the values which make
the intermediate word facet-complete are exactly the Boolean interval

\[
       L_{d,p,b}\subseteq x\subseteq R_{d,p,b}.          \tag{4.3}
\]

For the provider-first branch, (4.3) must additionally be intersected with
the union of the exact service intervals for the original holes.  This is
the survivor-bit characterization already audited on D3.

All three ingredients in (4.2) depend on the deletion:

1. the original hole family `H_d`;
2. the witness-core family `V_{d,p}`;
3. the compatible seam contexts `C^d_t(p)`.

Thus the 16 facet labels are deletion-independent, but their literal
first-edit domains are not.  This is the precise obstruction to replacing
the 191-row D4 census by a single deletion-blind Boolean interval.

There is also an authenticated counterexample to the tempting rule that the
survivor bit must be common to the original deletion holes.  Put

\[
       K_d=\bigcap_{h\in H_d}h.
\]

Across the seven D3 basins, exactly 2,754 provider-first actions with
`J(Z) != 0` satisfy

\[
       J(Z)\cap K_d=\varnothing.                         \tag{4.4}
\]

The per-deletion counts are

```text
d=0:352, d=1:263, d=3:228, d=6389:1143,
d=6441:524, d=12871:127, d=12873:117.
```

In these rows the first edit services every original hole which omits the
eventual survivor bit, while newly ejected targets supply the common residual
bit.  Therefore neither `K_d` nor the deleted source cell canonically chooses
`b`.  The concentration of most other D3 actions on `K_d` is empirical only
and cannot be used as a pruning theorem.

## 5. Consequence for a global `+1` proof

The survivor index yields the following sound global template:

1. choose one of 16 bits `b` (or a nonzero filter generator `y`);
2. classify one-edit intermediate words satisfying the segmented facet cover
   (3.1);
3. apply the exact second-site target-core condition inside that class.

For the fixed parent `U`, extending the D4 computation to every deletion is
exactly such a theorem and would close the entire delete-plus-two-substitution
neighborhood of `U`.  It still would not prove `nu(16)>=12874`: an arbitrary
length-12873 universal word need not be a deletion-plus-two-substitution of
this particular `U`.

Accordingly, the minimal additional structural input for a genuine global
`+1` proof is one of:

* a normalization theorem placing every putative length-12873 word in this
  fixed-parent neighborhood; or
* a deletion-independent lower bound for the segmented facet covers (3.1)
  which is strong enough to contradict the remaining global length/waste
  ledger.

Neither statement follows from D3/D4.  The exact surviving coupling is
principal-filter/facet completeness; the exact failed shortcut is any rule
that assigns the facet bit from the original deletion-hole intersection.
