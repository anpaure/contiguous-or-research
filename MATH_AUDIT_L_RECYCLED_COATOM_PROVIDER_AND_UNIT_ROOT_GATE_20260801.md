# Independent audit: recycled coatom providers and the unit-root gate

Date: 2026-08-01  
Audited target:
`MATH_THEOREM_L_RECYCLED_COATOM_PROVIDER_AND_UNIT_ROOT_GATE_20260801.md`  
Audited target SHA-256:
`add8ba29523562d9f06ca583012c9d40943b88591cf4577e9656ef49951c50d8`  
Verdict: **PASS_WITH_EXPLICIT_STATIC_TYPE_LITERAL_SCOPE_SEPARATION**.

This audit is purely mathematical.  It uses no finite search and makes no
claim that the labelled pull-clock already contains the returned unit-root
catalogue of the positive theorem.

## 1. Exact finite-token cut

For a sink-side target set `B`, the proposed flow network cuts

* `s(B)` old-surplus source capacity;
* `c(P-B,B)` private transport capacity;
* one unit for exactly those occurrence tokens whose menu meets `B`; and
* `|D intersect (P-B)|` old-hole sink arcs.

Thus subtracting the minimum cut from `|D|` gives

\[
 \max_{B\subseteq P}
 (|D\cap B|-s(B)-c(P-B,B)-\gamma(B))_+.
\]

The direction of the transport cut and the definition
`gamma(B)=|{g:E_g intersect B nonempty}|` are correct.  The identity

\[
 |D\cap B|-s(B)=|B|-m(B)
\]

checks pointwise for `m=0`, `m=1`, and `m>=2`.

The proof was tightened during audit.  An arbitrary legal sequence need not
itself be a source-rooted flow, because it may first transport the sole
provider of a covered target.  The final statement now traces every newly
filled old hole backward to an initial surplus or consumed token and deletes
cycles and lineages ending at already covered targets.  That normal form is
exactly the displayed network flow, while forward path execution is safe.

## 2. Returned separator

A literally returned separator is correctly treated as a catalyst rather
than a positive source token.  Giving its primitive transfer arcs unbounded
reusable capacity leaves only in-closed target sets in the min-cut, so

\[
 H^*=\max_{\delta_R^-(B)=\varnothing}(|B|-m(B))_+.
\]

Forward execution of integral surplus-to-hole paths is valid: an
intermediate target receives the travelling unit before passing it on, and
the catalyst returns between moves.  Strong connectivity leaves only the
whole-palette cut; hence total load at least `|P|` is sufficient for zero
debt under the stated regeneration hypotheses.  No claim is made for a
separator-consuming or bundled macro.

## 3. Static coatom Hall theorem

Put `W=binom(k,r)`, `N=binom(k,r-1)<=W`, and assume the unpunctured coatom
row `b_(r-1)=0`, `q_(r-1)=N/W`.  For the supported owner--coatom mass
`X(T,Q)`, the fractional target-load formula gives

\[
 \sum_TX(T,Q)=1,
\]

while uniform owner mass and the uniqueness of a fixed-rank prefix give

\[
 \sum_QX(T,Q)=N/W\le1.
\]

Therefore, for every coatom family `S`,

\[
 |S|\le(N/W)|N_X(S)|\le|N_X(S)|,
\]

which is Hall on the positive support.  The odd/even central counts in the
theorem are exact.  The same argument is sound rank by rank on an
unpunctured row, but it does not combine those matchings into a common nested
flag.

The protected-`PH` consequence was also scope-corrected: global release and
rematching do not redefine the earlier `B_out`; they invalidate that
theorem's bounded-outside-bank premise by introducing a different global
matching layer.

## 4. `K=1` type-level fusion

For `d>=1`, `r>=d+3`, the two raw banks have exact sizes

\[
 \binom{r-1}{d},\qquad \binom{r-2}{d}.
\]

The second-bank type map
`iota(y)=(1+y_0,y_1,...,y_d)` is injective, and
`iota(y)->iota(Ry)` obeys the first shifted inequality
`y_0<=1+y_0` with equality thereafter.  The bipartite necklace graph is
connected: its `r`-shore two-section contains the connected positive-
composition unit-transfer graph, and every `(r-1)`-necklace `[y]` is
adjacent to `[y+e_0]`.

Crossing two current outgoing arcs from equal **types** remains legal after
earlier crossings, so a parent witness may be reused while a rooted
spanning tree is processed.  Exactly
`|A_r/<R>|+|A_(r-1)/<R>|-1` crossings merge all raw cycles.  This preserves
occurrence-attached marks only.  Equal type is not a labelled recurrence
rectangle, so the theorem correctly stops before named owners, arc payloads,
and compiler guards.

The coatom-capacity row is also exact: one `g_(0,b)` package has
`binom(b-1,d-1)` occurrences with final mobile part one, a fraction `d/b`
of the package.  Such an occurrence can be counted at most once at terminal
time.

## 5. Sharp obstruction checks

For bundled moves `q(e_v-e_u)`, all integral loads stay zero modulo `q`.
With total mass `qn`, at most `n` of `qn` targets can be present, so the
integral debt is at least `(q-1)n`; the initial state attains it.  Fractional
weight `1/q` on `q-1` private moves per source gives the all-one vector.
This is an exact nonsaturated-root-lattice obstruction, scoped as an
abstract provider catalogue.

For two globally synchronized unit-token phases, the averaged cut function
is `bar gamma(B)=|B|`, but either integral phase misses one shore of `n`
targets.  Hence the clock phase must remain inside the min--max.

Finally, the literal even-`k`, `(r,d)=(2,1)` family has exact stationary
coatom load one, while every one-copy selection orients `K_k` and has odd
divergence at all `k` states.  The circuit/open route lower bounds
`k/2` and `k/2-1` follow and are sharp.  This is infinite and literal but is
central only at `k=4`, exactly as scoped.

## 6. Audited conclusion

The proof-safe conclusion is the three-level split claimed by the theorem:

1. pull-clock high mass closes the **static** coatom provider Hall row;
2. one adjacent high package closes one core-free bank's **unlabelled type**
   topology; but
3. zero physical boundary requires transition-transparent retiming or a
   serializable, saturated, returned-separator unit-root network on the same
   one-copy chronology.

The fractional circulation alone proves neither item 3 nor a full nested-
flag/common-cap/compiler lift.

Detailed independent proof sources:

* `MATH_THEOREM_L_K1_HIGH_SEPARATOR_UNIVERSAL_TYPE_FUSION_20260801.md`,
  SHA-256
  `b3955b9320b90579a8df03d3eb9f628f971bd645193e49b6e9920c56d9527970`;
* `scratch/laneL_shared_provider_minmax_memo_20260801.md`, SHA-256
  `db6ecf495243f135b690b346ee9424c787162cf919a84551d749907e5d58720f`.
