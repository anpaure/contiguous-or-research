# K17 drop-12 S47 source / single-N-helper occurrence no-go

**Date:** 2026-08-03  
**Status:** exact, frozen, independently audited.

## Theorem

On the canonical parent

```text
compressed  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
final       fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
```

let `s` be one of the 47 authenticated S modes and `n` one of the seven N
modes. No endpoint-disjoint child has an exact two-phase source option for
`s` whose only external installed-host support is `h_n`.

Equivalently, an S source with exactly one N helper is occurrence-dead.

## Exact certificate

The complete directed structural prefix domain has

\[
 47\cdot7=329
\]

rows, with zero endpoint conflicts. For every row, the H100 checker deletes
both donors, inserts both hosts at all four flags, excludes the private 7,213
rows, applies the separate 20/20 phase reservations with intersection 17 and
union 23, and exhausts all 90 declared keys and both ticket sides.

Its rejection test is intentionally permissive: it asks only whether one
declared key has a physical phase-0 ticket and a physical phase-1 ticket. It
does not require cross-phase flag consistency or a helper-role option. Every
exact source prefix must therefore survive this upper.

The exact replay is

\[
 \boxed{329\longrightarrow0}.
\]

Frozen hashes:

```text
producer source       02e946595b4db261dc278206566e0a663fa7dfa7381dbff530ee41daefd4fe87
H100 binary           3899c788ecde7c2f85d1f952398aae31d22ca5da378edbc34a0fe74e7a59acc8
RUN_INPUTS            ccf3c6bd4470ecd657732f13bd423cf8ecdd9e4a7f7e19d81656f99005fcd281
empty upper TSV       534180a4038eb404d7c649ed279f1d9538691e50d43d2194871a6c4892a92feb
upper audit           891d979201f141400538f5eaa5f91fd8e835066d421394e19bc14a361f358bdf
OUTPUTS               7424dd0f43edc1bc47ed750453364329a66769454539b10fd65cd9a28db2d89e
FINAL_MANIFEST file   0c4e2b404bb1d8f8bc3a0cea50a45def575cfad8cde51598bb5e29f1bbf7289f
independent audit     2a33d3e228b21022a7e8631c914de7f0e3e1e5c09936b71e608a550b85c53997
independent manifest  e17e72caf098a59cd45d1b51455acaffe958f9032de90b9c921237251596dacf
```

The authoritative H100 root is
`/home/amodo/or15/work/codex_019fc39a_k17_s47_n_prefix_aperture_20260803`.
The self-contained local mirror is
`scratch/codex_019fc39a_k17_s47_n_prefix_aperture_20260803`.

## Restriction and lift

Suppose a larger endpoint-disjoint child contains `s,n` and additional mode
`g`, while the source option uses `h_n` but no other new helper host. Its
footprint satisfies

\[
 F(o_s)\cap\{h_g,d_g\}=\varnothing.                    \tag{1}
\]

Deleting transfer `g` therefore leaves the same physical tickets, key and
flags in the `S x N` pair child, contradicting the empty prefix relation.

Conversely, a fixed pair prefix lifts unchanged after adding `g` exactly
when condition (1) holds. Although an unselected LR host `h_g` is not a long
provider in the canonical pair bank, both rows remain explicit in the replay
contract.

## Scope

This theorem makes no claim about an S source supported only by another S
mode, an S source using both helpers, H-containing triples, complete supplier
rank, chronology, residence, upper coverage, compiler feasibility, or a K17
word. Closing S,S,N support-one requires combining this theorem with the
separate complete `S x (S union Z)` prefix theorem; bilateral production is a
separate conditional theorem.
