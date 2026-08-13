# Audit: universal labelled pair-cell target portals

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_PAIR_CELL_UNIVERSAL_TARGET_PORTALS_AND_SUBEXPONENTIAL_LOW_BANK_20260813.md`  
**Source SHA-256:**
`03b39753c82c68ced8778e051d16b114e68220ac3cc7d2944f45f7cd5cd3cc04`  
**Verdict:** **PASS after proof-exposition clarifications**.  The local
existence theorem is valid; its fractional and integral scope boundaries
are necessary.

## 1. Middle programmable ranks

For a target `S` of rank `s` in

\[
                         h+1\le s\le R-q,
\]

the proposed dimension

\[
                         m=s+q-1
\]

satisfies `M=q+h<=m<=R-1=p`, so it is a good pair-cell dimension.
Choose the sentinel outside `S`.  At a pointed address of any long-run
`m`-cube Gray cycle, the preceding `q-1` directions are distinct.  A
coordinate permutation of the cube lets those directions be assigned to
any prescribed `q-1` singleton pairs.

Use `s=m-q+1` untouched singleton pairs with selected sides equal to the
elements of `S`, and use `q-1` transition pairs entirely outside `S`.
Together with the sentinel this uses

\[
                         s+2(q-1)+1
\]

outside labels and leaves exactly `2(p-m)` labels.  The parity choice

\[
 \epsilon\equiv R-m\pmod2,qquad
 a={R-\epsilon-m\over2},qquad b=p-m-a
\]

makes `a,b` nonnegative integers with `a+b=p-m`; the remaining pairs may
therefore be declared double or empty.  These pairs and the sentinel are
the permanent core and all lie outside `S`.

Across the pointed `q` owners, each transition pair contributes neither
endpoint to the intersection, while each untouched singleton contributes
its fixed selected side.  Thus `B_t=S` literally.  A `(q-1)`-hitting
schedule can avoid one singleton source address for `q>=3`, so the
three-shore-preserving assertion is also valid.

## 2. Top programmable-letter rank

At `s=R-q+1`, take `m=p` and sentinel `z in S`.  The sentinel-present
sector has

\[
                         C=\{z\},qquad a=b=0.
\]

The `p-q+1=s-1` untouched singleton pairs contribute `S-{z}` and the
remaining `q-1` pairs are transition directions.  The outside-label count
is exact:

\[
 (s-1)+2(q-1)=R+q-2=k-s.
\]

Hence the complement supplies precisely the mates and transition labels;
emitting `z` at the marked address gives `S`.  The endpoint `m=p` is not a
parity exception.

## 3. Top fan ranks

For `R-q+2<=s<=R-1`, put `r=R-s`, so `1<=r<=q-2`.  Again use `m=p` and
the sentinel-present sector.  Relabel `r` consecutive, hence distinct,
Gray directions as transition pairs.  The untouched pairs contribute the
`s-1` elements of `S-{z}`.  The complement count

\[
                         (s-1)+2r=p+r=k-s
\]

is exact.  Therefore the intersection of the `r+1` consecutive owners is
`S`.

The maximal-antecedent identity transports this owner intersection to a
literal source interval of width `q-r`.  Since `r>=1`, this width is at
most `q-1`; since `r<=q-2`, it is at least two.  The pointed transition
block exists in every long-run Hamilton cycle; only coordinate relabelling,
not a new Gray-code existence assertion, is used.

## 4. Exceptional target bank

The three rank ranges cover every strict-lower rank from `h+1` through
`R-1`.  The remaining values have ranks `1,...,h`, and

\[
 \sum_{s=1}^h\binom{2p+1}s
 \le h\left({e(2p+1)\over h}\right)^h
 =\exp(O((\log p)^2))=W^{o(1)}.
\]

This is a value count only.  It neither makes the bank `O(1)` nor absorbs
the exponentially large low-dimensional **owner** leave.

## 5. Fractional scope

Taking the full symmetric-group orbit of one pointed portal is transitive
on the named rank-`s` targets.  Uniform weight therefore gives a literal
fractional one-cover of that target row.  This averaging changes the pair
partition, cell, and owner factor, so it does not place portals for
different targets in one integral factor.  The source correctly leaves
the simultaneous interval cap, interval injectivity, bad-owner absorption,
and fusion open.

## 6. Conclusion

No label-count, parity, `m=p` endpoint, or pointed-transition flaw remains
in the clarified source.  The safe theorem is

\[
 \boxed{
 |S|\ge h+1
 \Longrightarrow
 \text{some labelled good pair-cell portal for }S,
 }
\]

together with symmetric fractional target-row coverage.  It is not an
integral common-factor theorem.

The standard-library replay
`verify_pair_cell_universal_portal_label_counts.py`, SHA-256
`b9854e2058e3537b1e8cdc41ec10d8ff06bbd9de7447ad7856ab6fc9831b7a4e`,
checked all displayed parity and label-exhaustion identities at
`k=101,201,301,401,641,1001` on `h100` and returned `PASS`.
